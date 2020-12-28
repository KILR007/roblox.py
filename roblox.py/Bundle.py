


from .utils import send_request

from .exceptions import BundleNotFound
class BundleInfo:
    def __init__(self, bundleID:int,json_obj):
        idkdd = isinstance(bundleID, str)
        if idkdd:
            raise TypeError(f"{bundleID} must be an integer")
        if "id" not in json_obj.keys():
            raise BundleNotFound
        self._id = bundleID
        self.Noob = json_obj
    @property
    def name(self):
        idk = self.Noob
        return idk["name"]

    def __repr__(self):
        return self.name

    @property
    def id(self):
        return self._id

    @property
    def description(self):
        idk = self.Noob
        return idk["description"]

    @property
    def thumbnail(self):
        eep = await send_request(url=f"https://thumbnails.roblox.com/v1/bundles/thumbnails?bundleIds={self._id}&size=420x420&format=Png&isCircular=false")
        return eep["data"][0]["imageUrl"]

    @property
    def bundle_creator(self):
        idk = self.Noob
        return idk["creator"]["name"]

    @property
    def direct_url(self):
        return f"https://www.roblox.com/bundles/{self.id}/"

    @property
    def price(self):
        idk = self.Noob
        return idk["product"]["priceInRobux"] if not None else 0

    @property
    def Is_for_sale(self):
        idk = self.Noob
        return idk["product"]["isForSale"]

    @property
    def type(self):
        idk = self.Noob
        return idk["bundleType"]
