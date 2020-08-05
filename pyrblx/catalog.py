


import requests
class Badarguement(Exception):
    """Raised When Site Returns Status Code Other Than 200"""
class Bundlenotfound(Exception):
    """ Raised When Bundle Is Not Found"""





bundle_id1 =None
xd = None

class Bundles:
    def __init__(self,bundle_id:int):
        global bundle_id1
        bundle_id1 = bundle_id
        self.bundle_id = bundle_id
        global xd
        xd = requests.get(f"https://catalog.roblox.com/v1/bundles/{bundle_id}/details").json()
        if "id" not in xd.keys():
            raise Bundlenotfound


    @staticmethod
    def bundle_name():
        return xd["name"]
    @staticmethod
    def description():
        return xd["description"]
    @staticmethod
    def bundle_creator_name():
        return xd["creator"]["name"]
    @staticmethod
    def bundle_creator_id():
        return xd["creator"]["id"]
    @staticmethod
    def price():
        return xd["product"]["priceInRobux"]
    @staticmethod
    def isforsale():
        return xd["product"]["isForSale"]
    @staticmethod
    def type():
        return xd["bundleType"]