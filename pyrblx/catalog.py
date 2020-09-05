from .exceptions import BundleNotFound
from .utils import *
class Bundle:
    def __init__(self,ID:int):
        self.id = ID
        xddd = isinstance(ID,str)
        if xddd:
            raise TypeError

        self.Noob = direct(f"https://catalog.roblox.com/v1/bundles/{ID}/details")
        if "id" not in self.Noob.keys():
            raise BundleNotFound
class Bundles(Bundle):
    def bundle_name(self):
        xd = self.Noob
        return xd["name"]


    def description(self):
        xd = self.Noob
        return xd["description"]


    def bundle_creator_name(self):
        xd = self.Noob
        return xd["creator"]["name"]


    def bundle_creator_id(self):
        xd = self.Noob
        return xd["creator"]["id"]


    def price(self):
        xd = self.Noob
        return xd["product"]["priceInRobux"]


    def isforsale(self):
        xd = self.Noob
        return xd["product"]["isForSale"]


    def type(self):
        xd = self.Noob
        return xd["bundleType"]
