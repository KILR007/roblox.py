

import datetime
from .exceptions import GamePassNotFound
from .Classes import Time, PartialInfo


class GamepassInfo:
    """

    Represents a ROBLOX Game Pass.

    """

    def __init__(self, request, gamepassID: int):
        self.request = request
        idkdd = isinstance(gamepassID, str)
        if idkdd:
            raise TypeError(f"{gamepassID} must be an integer")

        self._id = gamepassID
        self._json_obj = None

    async def update(self):
        r = await self.request.request(url=f"http://api.roblox.com/marketplace/game-pass-product-info?gamePassId={self._id}", method='get')
        if "TargetId" not in r.keys():
            raise GamePassNotFound
        self._json_obj = r

    @property
    def product_type(self):
        return self._json_obj["ProductType"]

    @property
    def name(self) -> str:
        """
        Returns Game-pass Name

        """
        return self._json_obj["Name"]

    @property
    def id(self) -> int:
        """
        Returns Game-pass ID

        """
        return self._json_obj["TargetId"]

    def __repr__(self):
        return self.name

    @property
    def description(self) -> str:
        """
        Returns Game-pass Description

        """
        return self._json_obj["Description"]

    @property
    def creator(self) -> PartialInfo:
        """
        Returns Creator Information
        """
        if self._json_obj["Creator"]['CreatorType'] == "Group":

            return PartialInfo(
                id=self._json_obj["Creator"]["CreatorTargetId"],
                name=self._json_obj["Creator"]["Name"])
        else:
            return PartialInfo(
                name=self._json_obj["Creator"]["Name"],
                id=self._json_obj["Creator"]["CreatorTargetId"])

    @property
    def creator_type(self) -> str:
        """
        Returns Creator Type (Group/User)
        """
        return self._json_obj["Creator"]["CreatorType"]

    @property
    def price_in_robux(self) -> int:
        """
        Returns Bundle Price( 0 if free)
        """
        return self._json_obj["PriceInRobux"] if not None else 0

    @property
    def created_at(self) -> str:
        """
        Gives the created date in iso8601  format
        """
        return self._json_obj["Created"]

    def created_age(self) -> Time:
        """
        Returns last created time from current time
        """
        date_time_str = self._json_obj["Created"]
        noob = date_time_str[:10]
        strp = datetime.datetime.strptime(noob, '%Y-%m-%d')
        now = datetime.datetime.utcnow()
        diff = now - strp
        days = diff.days
        months, days = divmod(days, 30)
        yrs, months = divmod(months, 12)
        return Time(yrs=yrs, month=months, day=days)

    @property
    def updated_at(self):
        """
        Gives the last updated date in iso8601 format
        """
        return self._json_obj["Updated"]

    @property
    def update_age(self):
        """
        Returns last updated time from current time
        """
        date_time_str = self._json_obj["Updated"]
        noob = date_time_str[:10]
        strp = datetime.datetime.strptime(noob, '%Y-%m-%d')
        now = datetime.datetime.utcnow()
        diff = now - strp
        days = diff.days
        months, days = divmod(days, 30)
        yrs, months = divmod(months, 12)
        return Time(yrs=yrs, month=months, day=days)

    @property
    def sales(self) -> int:
        """
        Gets the Number of Sales of the item
        """
        return self._json_obj["Sales"]

    @property
    def buyable(self) -> bool:
        """

        Returns True if the item is on sale

        """
        return self._json_obj["IsForSale"]

    @property
    def is_limited(self) -> bool:
        """

        Check if the item is limited


        """
        return self._json_obj["IsLimited"]

    @property
    def direct_url(self) -> str:

        """
        Returns direct ROBLOX URL of the gamepass
        """
        return f'https://www.roblox.com/game-pass/{self._id}/'

    @property
    def is_limited_unique(self) -> bool:
        """
        Check if the item is limited

        """
        return self._json_obj["IsLimitedUnique"]

    @property
    def remaining(self):
        """
        Returns Remaining
        """
        return self._json_obj["Remaining"]

    @property
    async def thumbnail(self) -> str:
        """
        Returns Thumbnail Link
        """
        _ok = await self.request.request(url=f"https://thumbnails.roblox.com/v1/game-passes?gamePassIds={self._id}&size=150x150&format=Png", method='get')
        return _ok["data"][0]['imageUrl']

    @property
    def product_id(self) -> int:
        """
        Returns Product ID
        """
        return self._json_obj['ProductId']
