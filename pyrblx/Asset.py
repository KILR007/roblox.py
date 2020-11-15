
from .Exceptions import AssetNotFound
from .Utils import sendreq,direct
import datetime


class AssetInfo:
    def __init__(self,assetID:int):
        self.ID = assetID
        self.link = direct(f"http://api.roblox.com/Marketplace/ProductInfo?assetId={self.ID}")
        if "AssetId" not in self.link.keys():
            raise AssetNotFound

    @property
    def product_Type(self):
        return self.link["ProductType"]

    @property
    def name(self):
        return self.link["Name"]

    def __repr__(self):
        return self.name

    @property
    def description(self):
        return self.link["Description"]

    @property
    def creator_name(self):
        return self.link["Creator"]["Name"]

    @property
    def creator_Type(self):
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
    def updated(self):
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
    def IsLimited(self):
        return self.link["IsLimited"]

    @property
    def IsLimitedUnique(self):
        return self.link["IsLimitedUnique"]

    @property
    def remaining(self):
        return self.link["Remaining"]

    @property
    def icon(self):
        _ok = sendreq(f"https://www.roblox.com/item-thumbnails?params=%5B%7BassetId:{self.ID}%7D%5D")
        return _ok[0]["thumbnailUrl"]

    @property
    def thumbnail(self):
        return f"https://assetgame.roblox.com/Game/Tools/ThumbnailAsset.ashx?aid={self.ID}&fmt=png&wd=420&ht=420"

    @property
    def direct_url(self):
        return f"https://www.roblox.com/games/{self.ID}/{self.name}"