
import requests
class Bundlenotfound(Exception):
    """ Raised When Bundle Is Not Found"""
class Badarguement(Exception):
    """Raised When Site Returns Status Code Other Than 200"""
xd = None
iddd = None
bundle_id1 = None
def sendreq(url):
    pp = requests.get(url)
    if pp.status_code == 200:
        return pp.json()
    else:
        raise Badarguement
class Bundles:
    def __init__(self,bundle_id:int):
        global bundle_id1
        bundle_id1 = bundle_id
        self.bundle_id = bundle_id
        global xd
        xd = sendreq(f"https://catalog.roblox.com/v1/bundles/{bundle_id}/details")
        if "id" not in xd.keys():
            raise Bundlenotfound
    @staticmethod
    def bundle_id():
        return iddd
    @staticmethod
    def bundle_name():
        xd = sendreq(f"https://catalog.roblox.com/v1/bundles/{bundle_id1}/details")
        return xd["name"]
    @staticmethod
    def description():
        xd = sendreq(f"https://catalog.roblox.com/v1/bundles/{bundle_id1}/details")
        return xd["description"]
    @staticmethod
    def bundle_creator_name():
        xd = sendreq(f"https://catalog.roblox.com/v1/bundles/{bundle_id1}/details")
        return xd["creator"]["name"]
    @staticmethod
    def bundle_creator_id():
        xd = sendreq(f"https://catalog.roblox.com/v1/bundles/{bundle_id1}/details")
        return xd["creator"]["id"]
    @staticmethod
    def price():
        xd = sendreq(f"https://catalog.roblox.com/v1/bundles/{bundle_id1}/details")
        return xd["product"]["priceInRobux"]
    @staticmethod
    def isforsale():
        xd = sendreq(f"https://catalog.roblox.com/v1/bundles/{bundle_id1}/details")
        return xd["product"]["isForSale"]
    @staticmethod
    def type():
        xd = sendreq(f"https://catalog.roblox.com/v1/bundles/{bundle_id1}/details")
        return xd["bundleType"]

