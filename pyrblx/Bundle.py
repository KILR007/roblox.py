from .Exceptions import BundleNotFound
from .Utils import *
from .Player import PlayerInfo


class BundleInfo:
    def __init__(self, bundleID: int):
        self._id = bundleID
        idkdd = isinstance(bundleID, str)
        if idkdd:
            raise TypeError

        self.Noob = direct(f"https://catalog.roblox.com/v1/bundles/{bundleID}/details")
        if "id" not in self.Noob.keys():
            raise BundleNotFound

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
        eep = sendreq(f"https://thumbnails.roblox.com/v1/bundles/thumbnails?bundleIds={self._id}&size=420x420&format=Png&isCircular=false")
        return eep["data"][0]["imageUrl"]

    @property
    def bundle_creator(self):
        idk = self.Noob
        return PlayerInfo(idk["creator"]["name"])

    @property
    def direct_url(self):
        return f"https://www.roblox.com/bundles/{self.id}/"

    @property
    def price(self):
        idk = self.Noob
        return idk["product"]["priceInRobux"] if not None else 0

    @property
    def Isforsale(self):
        idk = self.Noob
        return idk["product"]["isForSale"]

    @property
    def type(self):
        idk = self.Noob
        return idk["bundleType"]
