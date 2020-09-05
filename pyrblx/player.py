from .utils import sendreq,direct
from .exceptions import PlayerNotFound
class Player:
    def __init__(self,username:str):
        username = str(username)
        self.username = username
        url = f"https://api.roblox.com/users/get-by-username?username={self.username}"
        noob = direct(url)
        if "Id" not in noob.keys():
            raise PlayerNotFound
        else:
            self.dat = noob["Id"]
            self.friendship = sendreq(f"https://friends.roblox.com/v1/users/{self.dat}/friends")
            self.groupsss = sendreq(f"https://api.roblox.com/users/{self.dat}/groups")
            self.descsss = sendreq(f"https://users.roblox.com/v1/users/{self.dat}")
            self.badgessss = sendreq(f"https://www.roblox.com/badges/roblox?userId={self.dat}")
class Players(Player):

    def user_name(self):
        return self.descsss["name"]
    @classmethod
    def get_by_id(cls,other:int):
        cc = isinstance(other,str)
        if cc:
            raise TypeError
        xd = direct(f"https://api.roblox.com/users/{other}")
        if "Username" not in xd.keys():
            raise PlayerNotFound
        else:
            return cls(xd["Username"])
    def user_id(self):
        return self.dat
    def description(self):
        oof = self.descsss["description"]
        if oof == "":
            return None
        return oof
    def created_at(self):
        oof = self.descsss["created"]
        if oof == "":
            return None
        return oof
    def roblox_badges(self):
        mm = self.badgessss
        string = []
        for item in mm["RobloxBadges"]:
            string.append(f'{item["Name"]}')
        if string == []:
            return None
        return string
    def direct_url(self):
        f = self.dat
        return f"https://www.roblox.com/users/{f}/profile"
    def friends(self):
        f = self.friendship
        lists = []
        for bill in f['data']:
            pp = bill.get('name')
            lists.append(pp)
        if lists == []:
            return None
        return lists
    def latest_friend(self):
        try:
            f = self.friendship
            return f["data"][0]["name"]
        except IndexError:
            return None
    def friends_count(self):
        p = self.friendship
        return len(p["data"])
    def oldest_friend(self):
        f = self.friendship
        if len(f["data"]) == 0:
            return None
        else:
            D = len(f["data"]) - 1
            return f["data"][D]["name"]
    def groups(self):
        f = self.groupsss
        lists = []
        for bill in f:
            pp = bill.get('Name')
            lists.append(pp)
        if lists == []:
            return None
        return lists
    def latest_group(self):
        f = self.groupsss

        try:
            return f[0]["Name"]
        except IndexError:
            return None

    def oldest_group(self):
        n = self.groupsss
        if len(n) == 0:
            return None
        else:
            D = len(n) - 1
            return n[D]["Name"]


    def groups_count(self):
        if len(self.groupsss) == 0:
            return 0
        else:
            return len(self.groupsss)
    def avatar(self):
        f = self.dat
        noob = sendreq(f"https://www.roblox.com/headshot-thumbnail/json?userId={f}&width=420&height=420")
        return noob["Url"]

    def thumbnail(self):
        f = self.dat
        noob = sendreq(f"https://www.roblox.com/headshot-thumbnail/json?userId={f}&width=180&height=180")
        return noob["Url"]






