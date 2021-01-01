
from .exceptions import BundleNotFound


class BundleInfo:
    def __init__(self, request,bundleID:int):
        self.request = request
        idkdd = isinstance(bundleID, str)
        if idkdd:
            raise TypeError(f"{bundleID} must be an integer")
        self._id = bundleID
        self.json_obj = None

    async def update(self):
        Noob = await self.request.request(url=f"https://catalog.roblox.com/v1/bundles/{self._id}/details",method='get')
        if "id" not in Noob.keys():
            raise BundleNotFound
        self.json_obj = Noob
    @property
    def name(self):
        idk = self.json_obj
        return idk["name"]

    def __repr__(self):
        return self.name

    @property
    def id(self):
        return self._id

    @property
    def description(self):
        idk = self.json_obj
        return idk["description"]

    @property
    async def thumbnail(self):
        eep = await self.request.request(url=f"https://thumbnails.roblox.com/v1/bundles/thumbnails?bundleIds={self._id}&size=420x420&format=Png&isCircular=false",method='get')
        return eep["data"][0]["imageUrl"]

    @property
    def bundle_creator(self):
        idk = self.json_obj
        return idk["creator"]["name"]

    @property
    def direct_url(self):
        return f"https://www.roblox.com/bundles/{self.id}/"

    @property
    def price(self):
        idk = self.json_obj
        return idk["product"]["priceInRobux"] if not None else 0

    @property
    def Is_for_sale(self):
        idk = self.json_obj
        return idk["product"]["isForSale"]

    @property
    def type(self):
        idk = self.json_obj
        return idk["bundleType"]
