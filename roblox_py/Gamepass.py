


import datetime
from .exceptions import GamePassNotFound

class GamepassInfo:
    def __init__(self,request,gamepassID:int):
        self.request = request
        idkdd = isinstance(gamepassID, str)
        if idkdd:
            raise TypeError(f"{gamepassID} must be an integer")

        self._id = gamepassID
        self.link = None

    async def update(self):
        r = await self.request.request(url=f"http://api.roblox.com/marketplace/game-pass-product-info?gamePassId={self._id}",method='get')
        if "TargetId" not in r.keys():
            raise GamePassNotFound
        self.link = r
    @property
    def product_type(self):
        return self.link["ProductType"]

    @property
    def name(self):
        return self.link["Name"]

    @property
    def id(self):
        return self.link["TargetId"]

    def __repr__(self):
        return self.name

    @property
    def description(self):
        return self.link["Description"]

    @property
    def creator(self):
        return self.link["Creator"]["Name"]

    @property
    def creator_id(self):
        return self.link["Creator"]["Id"]
    @property
    def creator_type(self):
        return self.link["Creator"]["CreatorType"]

    @property
    def price_in_robux(self):
        return self.link["PriceInRobux"] if not None else 0

    @property
    def created_at(self):
        return self.link["Created"]

    @property
    def created_age(self):
        date_time_str = self.link["Created"]
        noob = date_time_str[:10]
        strp = datetime.datetime.strptime(noob, '%Y-%m-%d')
        now = datetime.datetime.utcnow()
        diff = now - strp
        days = diff.days
        months, days = divmod(days, 30)
        yrs, months = divmod(months, 12)
        return dict(years=yrs, months=months, days=days)

    @property
    def updated_at(self):
        return self.link["Updated"]

    @property
    def update_age(self):
        date_time_str = self.link["Updated"]
        noob = date_time_str[:10]
        strp = datetime.datetime.strptime(noob, '%Y-%m-%d')
        now = datetime.datetime.utcnow()
        diff = now - strp
        days = diff.days
        months, days = divmod(days, 30)
        yrs, months = divmod(months, 12)
        return dict(years=yrs, months=months, days=days)

    @property
    def sales(self):
        return self.link["Sales"]

    @property
    def buyable(self):
        return self.link["IsForSale"]

    @property
    def is_Limited(self):
        return self.link["IsLimited"]
    @property
    def direct_url(self):
        return f'https://www.roblox.com/game-pass/{self._id}/'
    @property
    def is_Limited_Unique(self):
        return self.link["IsLimitedUnique"]

    @property
    def remaining(self):
        return self.link["Remaining"]

    @property
    async def thumbnail(self):
        _ok = await self.request.request(url=f"https://thumbnails.roblox.com/v1/game-passes?gamePassIds={self._id}&size=150x150&format=Png",method='get')
        return _ok["data"][0]['imageUrl']


    @property
    def product_id(self):
        return self.link['ProductId']
