import datetime
from .exceptions import AssetNotFound


class AssetInfo:
    def __init__(self,request,assetID:int):
        self.request = request
        idkdd = isinstance(assetID, str)
        if idkdd:
            raise TypeError(f"{assetID} must be an integer")

        self.ID = assetID
        self._json_obj = None

    async def update(self):
        r = await self.request.request(url=f"http://api.roblox.com/Marketplace/ProductInfo?assetId={self.ID}",method='get')
        if "AssetId" not in r.keys():
            raise AssetNotFound
        self._json_obj = r

    @property
    def product_type(self):
        return self._json_obj["ProductType"]

    @property
    def name(self):
        return self._json_obj["Name"]

    @property
    def id(self):
        return self._json_obj["TargetId"]


    def __repr__(self):
        return self.name

    @property
    def description(self):
        return self._json_obj["Description"]

    @property
    def creator(self):
        return self._json_obj["Creator"]["Name"]

    @property
    def creator_type(self):
        return self._json_obj["Creator"]["CreatorType"]

    @property
    def price_in_robux(self):
        return self._json_obj["PriceInRobux"] if not None else 0

    @property
    def created_at(self):
        return self._json_obj["Created"]

    @property
    def created_age(self):
        date_time_str = self._json_obj["Created"]
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
        return self._json_obj["Updated"]

    @property
    def update_age(self):
        date_time_str = self._json_obj["Updated"]
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
        return self._json_obj["Sales"]

    @property
    def buyable(self):
        return self._json_obj["IsForSale"]

    @property
    def is_Limited(self):
        return self._json_obj["IsLimited"]

    @property
    def is_Limited_Unique(self):
        return self._json_obj["IsLimitedUnique"]

    @property
    def remaining(self):
        return self._json_obj["Remaining"]

    @property
    def creator_id(self):
        return self._json_obj["Creator"]["Id"]
    @property
    async def icon(self):
        _ok = await self.request.request(url=f"https://www.roblox.com/item-thumbnails?params=%5B%7BassetId:{self.ID}%7D%5D",method='get')
        return _ok[0]["thumbnailUrl"]

    @property
    def thumbnail(self):
        return f"https://assetgame.roblox.com/Game/Tools/ThumbnailAsset.ashx?aid={self.ID}&fmt=png&wd=420&ht=420"

    @property
    def product_id(self):
        return self._json_obj['ProductId']
