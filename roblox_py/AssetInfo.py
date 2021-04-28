import datetime
from .exceptions import AssetNotFound
from .Classes import Time, PartialInfo


class AssetInfo:

    def __init__(self, request, asset_id: int):
        """

        Represents a ROBLOX asset.

        **Parameter**
        -------------

        request : roblox_py.Requests
            Request Class To Do HTTP Requests
        asset_id : int
            Asset ID
        """
        self.request = request

        self.ID = asset_id
        self._json_obj = None

    async def update(self):
        """
        Must be called before using the class else the class will misbehave.
        """
        r = await self.request.request(url=f"http://api.roblox.com/Marketplace/ProductInfo?assetId={self.ID}",
                                       method='get')
        if "AssetId" not in r.keys():
            raise AssetNotFound
        self._json_obj = r

    @property
    def product_type(self):
        """
        Returns Asset's Type
        """
        return self._json_obj["ProductType"]

    @property
    def name(self):
        """
        Returns Asset's Name
        """
        return self._json_obj["Name"]

    @property
    def id(self):
        """
        Returns Asset's ID
        """
        return self._json_obj["TargetId"]

    def __repr__(self):
        return self.name

    @property
    def description(self):
        """
        Returns Asset's Description
        """
        return self._json_obj["Description"]

    @property
    def creator(self):
        """
        Returns a partial info instance which contains the asset creator's name and ID.
        """
        if self.creator_type == 'Group':
            return PartialInfo(
                name=self._json_obj["Creator"]["Name"],
                id=self._json_obj["Creator"]["CreatorTargetId"])
        if self.creator_type == 'User':
            return PartialInfo(
                name=self._json_obj["Creator"]["Name"],
                id=self._json_obj["Creator"]["CreatorTargetId"])

    @property
    def creator_type(self):
        """
        Returns the asset creator's type (Group/User)
        """
        return self._json_obj["Creator"]["CreatorType"]

    @property
    def price_in_robux(self):
        """
        Returns Bundle Price(0 if free)
        """
        return self._json_obj["PriceInRobux"] if not None else 0

    @property
    def created_at(self):
        """
        Gives the created date in iso8601  format
        """
        return self._json_obj["Created"]

    def created_at_formatted(self) -> Time:
        """
        Returns Formatted Asset Creation Date
        """
        date_time_str = self.created_at
        noob = date_time_str[:10]
        strp = datetime.datetime.strptime(noob, '%Y-%m-%d')
        return Time(yrs=strp.year, month=strp.month, day=strp.day)

    def created_age(self):
        """
        Will return how long the asset has been up for.
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

    def updated_at_formatted(self) -> Time:
        """
        Returns a Time instance which contains the years, months, and days which contains formatted date
        """
        date_time_str = self.updated_at
        noob = date_time_str[:10]
        strp = datetime.datetime.strptime(noob, '%Y-%m-%d')
        return Time(yrs=strp.year, month=strp.month, day=strp.day)

    def update_age(self):
        """
        Returns a Time instance which contains the years, months, and days since the badge's last update.
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
    def sales(self):
        """
        Returns the asset's amount of sales.
        """
        return self._json_obj["Sales"]

    @property
    def buyable(self):
        """
        Returns if the asset is available for purchase.
        """
        return self._json_obj["IsForSale"]

    @property
    def is_limited(self):
        """
        Returns if the asset is limited.
        """
        return self._json_obj["IsLimited"]

    @property
    def is_limited_unique(self):
        """
        Returns if the asset is limited unique.
        """
        return self._json_obj["IsLimitedUnique"]

    @property
    def remaining(self):
        """
        Returns how many of the asset are left. Will return None if the asset is not limited.
        """
        return self._json_obj["Remaining"]

    async def icon(self):
        """
        Returns Asset's Icon Image Link
        """
        _ok = await self.request.request(
            url=f"https://www.roblox.com/item-thumbnails?params=%5B%7BassetId:{self.ID}%7D%5D", method='get')
        return _ok[0]["thumbnailUrl"]

    def thumbnail(self):
        """
        Returns Asset's Thumbnail Image Link
        """
        return f"https://assetgame.roblox.com/Game/Tools/ThumbnailAsset.ashx?aid={self.ID}&fmt=png&wd=420&ht=420"

    @property
    def product_id(self):
        """
        Returns the asset's product ID.
        """
        return self._json_obj['ProductId']
