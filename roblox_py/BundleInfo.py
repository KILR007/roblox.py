from .exceptions import BundleNotFound
from .Classes import PartialInfo


class BundleInfo:
    """
    
    Represents a ROBLOX Bundle.
    
    """

    def __init__(self, request, bundleID: int):
        self.request = request

        self._id = bundleID
        self._json_obj = None

    async def update(self):
        Noob = await self.request.request(url=f"https://catalog.roblox.com/v1/bundles/{self._id}/details", method='get')
        if "id" not in Noob.keys():
            raise BundleNotFound
        self._json_obj = Noob

    @property
    def name(self):
        idk = self._json_obj
        return idk["name"]

    def __str__(self):
        return self.name

    @property
    def id(self):
        return self._id

    @property
    def description(self):
        idk = self._json_obj
        return idk["description"]

    async def thumbnail(self):
        eep = await self.request.request(
            url=f'https://thumbnails.roblox.com/v1/bundles/thumbnails?bundleIds={self._id}&size=420x420&format=Png&isCircular=false',
            method='get')
        return eep["data"][0]["imageUrl"]

    @property
    def bundle_creator(self):
        idk = self._json_obj
        if idk["creator"]['type'] == "Group":
            return PartialInfo(id=idk["creator"]["id"], name=idk["creator"]["name"])
        elif idk["creator"]['type'] == "User":
            return PartialInfo(name=idk["creator"]["name"], id=idk["creator"]["id"])

    @property
    def direct_url(self):
        return f"https://www.roblox.com/bundles/{self.id}/"

    @property
    def price(self):
        idk = self._json_obj
        return idk["product"]["priceInRobux"] if not None else 0

    @property
    def is_for_sale(self):
        idk = self._json_obj
        return idk["product"]["isForSale"]

    @property
    def product_id(self):
        idk = self._json_obj
        return idk['product']['id']

    @property
    def product_type(self):
        idk = self._json_obj
        return idk["bundleType"]

    @property
    def creator_type(self):
        idk = self._json_obj
        return idk["creator"]["type"]
