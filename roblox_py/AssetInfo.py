import datetime
from .exceptions import AssetNotFound
from .Classes import Time,PartialInfo

class AssetInfo:
    """
    Represents a ROBLOX asset.
    
    Supported Operations
    --------------------
    str(a)
        Returns the asset's name
    
    Attributes
    ----------
    NAME  RETURN TYPE
    _________________
    product_type | int 
        Returns the asset's type ID.
    
    name | str
        Returns the asset's name.
    
    id | int
        Returns the asset's ID.
    
    description | str
        Returns the asset's description.
    
    creator | roblox_py.PartialInfo
        Returns a partial info instance which contains the asset creator's name and ID.
    
    creator_type | str
        Returns the asset creator's user type.
    
    price_in_robux | int
        Returns the asset's price.
    
    created_at | str
        Returns the asset's creation date.
     
    updated_at | str
        Returns the time of the asset's late update.
    
    sales | int
        Returns the asset's amount of sales.
    
    buyable | bool
        Returns if the asset is available for purchase.
        
    is_Limited | bool
        Returns if the asset is limited.
    
    is_Limited_Unique | bool
        Returns if the asset is limited unique.
    
    remaining | int
        Returns how many of the asset are left. Will return None if the asset is not limited.
    
    product_id | int
        Returns the asset's product ID.
       
    
    
    Methods
    -------
    TYPE      NAME       RETURN TYPE
    __________________________________
    def | created_age | roblox_py.Time
        Returns a Time instance which contains the years, months, and days the account has been up for.
    
    def | updated_age | roblox_py.Time
        Returns a Time instance which contains the years, months, and days since the asset's last update.
    
    def | thumbnail| str
        Returns the asset's thumbnail image link.
        
    async | icon | str
        Returns the asset's icon image link. 
    """
    
    def __init__(self,request,assetID:int):
        self.request = request

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


    def __str__(self):
        return self.name

    @property
    def description(self):
        return self._json_obj["Description"]

    @property
    def creator(self):
        if self.creator_type == 'Group':
            return PartialInfo(name=self._json_obj["Creator"]["Name"],id=self._json_obj["Creator"]["CreatorTargetId"])
        if self.creator_type == 'User':

            return PartialInfo(name=self._json_obj["Creator"]["Name"],id=self._json_obj["Creator"]["CreatorTargetId"])
            
    @property
    def creator_type(self):
        return self._json_obj["Creator"]["CreatorType"]

    @property
    def price_in_robux(self):
        return self._json_obj["PriceInRobux"] if not None else 0

    @property
    def created_at(self):
        return self._json_obj["Created"]

    def created_age(self):
        """
        Method
        ------
        Will return how long the asset has been up for.
        
        Returns
        ------
        roblox_py.Time 
            An instance of the Time class which contains the years, months and days attributes.
        
        """
        date_time_str = self._json_obj["Created"]
        noob = date_time_str[:10]
        strp = datetime.datetime.strptime(noob, '%Y-%m-%d')
        now = datetime.datetime.utcnow()
        diff = now - strp
        days = diff.days
        months, days = divmod(days, 30)
        yrs, months = divmod(months, 12)
        return Time(yrs=yrs,month=months,day=days)

    @property
    def updated_at(self):
        return self._json_obj["Updated"]

    def update_age(self):
        date_time_str = self._json_obj["Updated"]
        noob = date_time_str[:10]
        strp = datetime.datetime.strptime(noob, '%Y-%m-%d')
        now = datetime.datetime.utcnow()
        diff = now - strp
        days = diff.days
        months, days = divmod(days, 30)
        yrs, months = divmod(months, 12)
        return Time(yrs=yrs,month=months,day=days)

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

    async def icon(self):
        _ok = await self.request.request(url=f"https://www.roblox.com/item-thumbnails?params=%5B%7BassetId:{self.ID}%7D%5D",method='get')
        return _ok[0]["thumbnailUrl"]

    def thumbnail(self):
        return f"https://assetgame.roblox.com/Game/Tools/ThumbnailAsset.ashx?aid={self.ID}&fmt=png&wd=420&ht=420"

    @property
    def product_id(self):
        return self._json_obj['ProductId']
