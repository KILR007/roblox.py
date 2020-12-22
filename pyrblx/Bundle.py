


from .utis import send_request


class BundleInfo:
    def __init__(self, bundleID:int,json):
        self._id = bundleID
        self.Noob = json
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
        eep = send_request(url=f"https://thumbnails.roblox.com/v1/bundles/thumbnails?bundleIds={self._id}&size=420x420&format=Png&isCircular=false")
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
    def Isforsale(self):
        idk = self.Noob
        return idk["product"]["isForSale"]

    @property
    def type(self):
        idk = self.Noob
        return idk["bundleType"]
