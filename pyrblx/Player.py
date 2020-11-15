from .Utils import sendreq,direct,sendreqwithparsm
from .Exceptions import PlayerNotFound
import concurrent.futures
import datetime


class PlayerInfo:
    def __init__(self,username:str):
        username = str(username).strip()
        self._username = username

        url = f"https://api.roblox.com/users/get-by-username?username={self._username}"
        noob = direct(url)
        if "Id" not in noob.keys():
            raise PlayerNotFound

        else:
            self._dat = noob["Id"]
            with concurrent.futures.ThreadPoolExecutor() as exor:
                self._Ascsss = exor.submit(sendreq,f"https://users.roblox.com/v1/users/{self._dat}").result()
            self.friends = Friends(self._dat)
            self.following = Following(self._dat)
            self.followers = Follower(self._dat)
            self.groups = Groups(self._dat)

    @classmethod
    def get_by_id(cls, other: int):
        cc = isinstance(other, str)
        if cc:
            raise TypeError
        xd = direct(f"https://api.roblox.com/users/{other}")
        if "Username" not in xd.keys():
            raise PlayerNotFound
        else:
            return cls(xd["Username"])

    @property
    def name(self):
        return self._Ascsss["name"]

    def __repr__(self):
        return self.name

    @property
    def id(self):
        return self._dat

    @property
    def description(self):
        oof = self._Ascsss["description"]
        if oof == "":
            return None
        return oof

    @property
    def get_private_games(self):
        payload = {'sortOrder': "Asc", "limit": 100}
        link = f"https://games.roblox.com/v2/users/{self._dat}/games?accessFilter=Private"
        stuff = sendreqwithparsm(link,payload)
        _lists = []
        while True:
            for bill in stuff['data']:
                pp = bill.get('name')
                pp1 = bill.get("id")
                _lists.append(dict(name=pp,id=pp1))
            if stuff["nextPageCursor"] is None or stuff["nextPageCursor"] == "null":
                break
            payload = {'cursor': stuff["nextPageCursor"], "limit": 100, "sortOrder": "Asc"}
            stuff = sendreqwithparsm(link, payload)
        return _lists

    def _stats_games(self, format1):
        parms = {"limit": 100, "sortOrder": f"{format1}"}
        link = f"https://games.roblox.com/v2/users/{self._dat}/games?accessFilter=Private"
        stuff = sendreqwithparsm(link, parms)
        _lists = []
        if stuff['data'] is None or stuff['data'] == "null":
            return None
        try:
            return dict(name=stuff['data'][0]["name"],id=stuff['data'][0]["id"])
        except IndexError:
            return None
    @property
    def oldest_private_game(self):
        _lists = self._stats_games("Asc")
        try:
            return _lists
        except IndexError:
            return

    @property
    def latest_private_game(self):
        _lists = self._stats_games("Desc")
        try:
            return _lists
        except IndexError:
            return

    @property
    def created_at(self):
        oof = self._Ascsss["created"]
        if oof == "":
            return None
        return oof

    @property
    def account_age(self):
        date_time_str = self._Ascsss["created"]
        noob = date_time_str[:10]
        strp = datetime.datetime.strptime(noob, '%Y-%m-%d')
        now = datetime.datetime.utcnow()
        diff = now - strp
        days = diff.days
        months, days = divmod(days, 30)
        yrs, months = divmod(months, 12)
        return dict(years=yrs,months=months,days=days)

    @property
    def direct_url(self):
        f = self._dat
        return f"https://www.roblox.com/users/{f}/profile"

    @property
    def avatar(self):
        p = {
            "size" : "720x720",
            "format" : "Png",
        }
        noob = sendreqwithparsm(f"https://thumbnails.roblox.com/v1/users/avatar?userIds={self._dat}",p)
        return noob["data"][0]["imageUrl"]

    @property
    def thumbnail(self):
        f = self._dat
        noob = sendreq(f"https://www.roblox.com/headshot-thumbnail/json?userId={f}&width=180&height=180")
        return noob["Url"]


class Friends:
    def __init__(self,ID):
        self.ID = ID
        with concurrent.futures.ThreadPoolExecutor() as exor:
            self._count = exor.submit(sendreq, f"https://friends.roblox.com/v1/users/{self.ID}/friends/count").result()
            self._friendship = exor.submit(sendreq, f"https://friends.roblox.com/v1/users/{self.ID}/friends").result()

    @property
    def name(self):
        f = self._friendship
        _lists = [bill.get('name') for bill in f["data"]]
        return _lists

    @property
    def latest(self):
        try:
            f = self._friendship
            return f["data"][0]["name"]
        except IndexError:
            return None

    @property
    def count(self):
        ff = self._count
        return ff["count"]

    @property
    def oldest(self):
        f = self._friendship
        if len(f["data"]) == 0:
            return None
        else:
            D = len(f["data"]) - 1
            return f["data"][D]["name"]


class Badges:
    def __init__(self,ID):
        self._dat = ID
        self._badges = sendreq(f"https://www.roblox.com/badges/roblox?userId={self._dat}")

    @property
    def roblox_badges(self):
        mm = self._badges
        _lists = [item["Name"] for item in mm["RobloxBadges"]]
        return _lists

    def _stats(self,format1):
        f = self._dat
        parms = {"limit": 100, "sortOrder": f"{format1}"}
        link = f"https://badges.roblox.com/v1/users/{f}/badges"
        stuff = sendreqwithparsm(link, parms)
        _lists = []
        if stuff['data'] is None or stuff['data'] == "null":
            return None
        try:
            return stuff['data'][0]["name"]
        except IndexError:
            return None

    @property
    def badges(self):
        f = self._dat
        parms = {"limit": 100, "sortOrder": "Asc"}
        link = f"https://badges.roblox.com/v1/users/{f}/badges"
        stuff = sendreqwithparsm(link, parms)
        _lists = []
        if stuff['data'] is None or stuff['data'] == "null":
            return []

        while True:
            for bill in stuff['data']:
                pp = bill.get('name')
                _lists.append(pp)
            if stuff["nextPageCursor"] is None or stuff["nextPageCursor"] == "null":
                break
            payload = {'cursor': stuff["nextPageCursor"], "limit": 100, "sortOrder": "Asc"}
            stuff = sendreqwithparsm(link, payload)
        return _lists

    @property
    def count_badges(self):
        return len(self.badges) if not None else 0

    @property
    def latest_badge(self):
        _lists = self._stats("Desc")
        if _lists is None:
            return None
        try:
            return _lists
        except IndexError:
            return

    @property
    def oldest_badge(self):
        _lists = self._stats("Asc")
        if _lists is None:
            return None
        try:
            return _lists
        except IndexError:
            return


class Following:
    def __init__(self,ID):
        self._dat = ID
        parms = {"limit": 100, "sortOrder": "Asc"}
        self._link = f"https://friends.roblox.com/v1/users/{self._dat}/followings"

        with concurrent.futures.ThreadPoolExecutor() as exor:
            self._stuff = exor.submit(sendreqwithparsm,self._link,parms).result()
            self._count = exor.submit(sendreq,f"https://friends.roblox.com/v1/users/{self._dat}/followings/count").result()

    @property
    def name(self):
        link = self._link
        stuff = self._stuff
        _lists = []
        while True:
            for bill in stuff['data']:
                pp = bill.get('name')
                _lists.append(pp)
            if stuff["nextPageCursor"] is None or stuff["nextPageCursor"] == "null":
                break
            payload = {'cursor': stuff["nextPageCursor"], "limit": 100, "sortOrder": "Asc"}
            stuff = sendreqwithparsm(link, payload)
        return _lists

    def _stats(self, format1):
        parms = {"limit": 100, "sortOrder": f"{format1}"}
        link = self._link
        stuff = sendreqwithparsm(link, parms)
        _lists = []
        if stuff['data'] is None or stuff['data'] == "null":
            return None
        try:
            return stuff['data'][0]["name"]
        except IndexError:
            return None

    @property
    def latest(self):
        _lists = self._stats("Desc")
        if _lists is None:
            return None
        try:
            return _lists
        except IndexError:
            return

    @property
    def oldest(self):
        _lists = self._stats("Asc")
        if _lists is None:
            return None
        try:
            return _lists
        except IndexError:
            return

    @property
    def count(self):
        return self._count["count"]


class Follower:
    def __init__(self,ID):
        self._dat = ID
        parms = {"limit": 100, "sortOrder": "Asc"}
        self._link = f"https://friends.roblox.com/v1/users/{self._dat}/followers"
        with concurrent.futures.ThreadPoolExecutor() as exor:
            self._stuff = exor.submit(sendreqwithparsm, self._link, parms).result()
            self._count = exor.submit(sendreq,f"https://friends.roblox.com/v1/users/{self._dat}/followers/count").result()

    def _stats(self, format1):
        parms = {"limit": 100, "sortOrder": f"{format1}"}
        link = self._link
        stuff = sendreqwithparsm(link, parms)
        _lists = []
        if stuff['data'] is None or stuff['data'] == "null":
            return None
        try:
            return stuff['data'][0]["name"]
        except IndexError:
            return None

    @property
    def name(self):
        link = self._link
        stuff = self._stuff
        _lists = []
        while True:
            for bill in stuff['data']:
                pp = bill.get('name')
                _lists.append(pp)
            if stuff["nextPageCursor"] is None or stuff["nextPageCursor"] == "null":
                break
            payload = {'cursor': stuff["nextPageCursor"], "limit": 100, "sortOrder": "Asc"}
            stuff = sendreqwithparsm(link, payload)
        return _lists

    @property
    def latest(self):
        _lists = self._stats("Desc")
        if _lists is None:
            return None
        try:
            return _lists
        except IndexError:
            return

    @property
    def oldest(self):
        _lists = self._stats("Asc")
        if _lists is None:
            return None
        try:
            return _lists
        except IndexError:
            return

    @property
    def count(self):
        return self._count["count"]


class Groups:
    def __init__(self,ID):
        self._dat = ID
        self._groups = sendreq(f"https://api.roblox.com/users/{self._dat}/groups")

    @property
    def name(self):
        f = self._groups
        _lists = [bill.get('Name') for bill in f]
        if _lists is []:
            return None
        return _lists

    @property
    def latest(self):
        f = self._groups
        try:
            return f[0]["Name"]
        except IndexError:
            return None

    @property
    def oldest(self):
        n = self._groups
        if len(n) == 0:
            return None
        else:
            D = len(n) - 1
            return n[D]["Name"]

    @property
    def count(self):
        if len(self._groups) == 0:
            return 0
        else:
            return len(self._groups)

    @property
    def primary_group(self):
        ok = direct(f"https://groups.roblox.com/v1/users/{self._dat}/groups/primary/role")

        try:
            return dict(name=ok["group"]["name"],id=ok["group"]["id"])
        except KeyError:
            return None

