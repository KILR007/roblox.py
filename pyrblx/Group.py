from .Utils import sendreq,direct,sendreqwithparsm
from .Exceptions import GroupNotFound
import concurrent.futures


class GroupInfo:
    def __init__(self, groupID: int):
        self._ID = groupID
        xd = direct(f"https://api.roblox.com/groups/{groupID}")
        if "Name" not in xd.keys():
            raise GroupNotFound
        else:
            parms = {"limit": 100, "sortOrder": "Asc"}
            self._link = f"https://groups.roblox.com/v1/groups/{groupID}/users"
            self._link2 = f"https://games.roblox.com/v2/groups/4075327/games"
            with concurrent.futures.ThreadPoolExecutor() as exor:
                self._groupss = exor.submit(sendreq, f"https://groups.roblox.com/v1/groups/{groupID}").result()
                self.enimes = exor.submit(sendreq, f"https://api.roblox.com/groups/{groupID}/enemies").result()
                self.alies = exor.submit(sendreq, f"https://api.roblox.com/groups/{groupID}/allies").result()
                self._mem = exor.submit(sendreqwithparsm, self._link, parms).result()

    @property
    def allies(self):
        lala = self.alies
        if lala["Groups"] is []:
            return None
        else:
            _lists = [good.get("Name") for good in lala['Groups']]
            return _lists

    @property
    def enemies(self):
        lala = self.enimes
        if lala["Groups"] is []:
            return None
        else:
            _lists = [good.get("Name") for good in lala['Groups']]
            return _lists

    @property
    def name(self):
        return self._groupss["name"]

    def __repr__(self):
        return self.name

    @property
    def id(self):
        return self._groupss["id"]

    @property
    def owner(self):
        return self._groupss["owner"]["username"]

    @property
    def count(self):
        return self._groupss["memberCount"]

    @property
    def is_private(self):
        if self._groupss["publicEntryAllowed"] is True:
            return False
        else:
            return True

    @property
    def is_premium_only_entry(self):
        return self._groupss["isBuildersClubOnly"]

    @property
    def shout(self):

        try:
            if self._groupss["shout"]["body"] == "":
                return None
            else:
                return self._groupss["shout"]["body"]
        except TypeError:
            return None

    @property
    def shout_poster(self):
        try:
            if self._groupss["shout"]["body"] == "":
                return None
            else:
                return self._groupss["shout"]["poster"]["username"]
        except TypeError:
            return None

    @property
    def thumbnail(self):
        dc = sendreq(f"https://www.roblox.com/group-thumbnails?params=%5B%7BgroupId:{self._ID}%7D%5D")
        return dc[0]["thumbnailUrl"]

    @property
    def direct_url(self):
        dc = sendreq(f"https://www.roblox.com/group-thumbnails?params=%5B%7BgroupId:{self._ID}%7D%5D")
        return dc[0]["url"]

    @property
    def description(self):
        try:
            if self._groupss["description"] == "":
                return None
            else:
                return self._groupss["description"]
        except TypeError:
            return None

    @property
    def members(self):
        link = self._link
        mem = self._mem
        _lists = []
        while True:
            for bill in mem['data']:
                pp = bill.get("user", {}).get("username")
                print(pp)
                _lists.append(pp)
            if mem["nextPageCursor"] is None or mem["nextPageCursor"] == "null":
                break
            payload = {'cursor': mem["nextPageCursor"], "limit": 100, "sortOrder": "Asc"}
            mem = sendreqwithparsm(link, payload)
        return _lists

    def _stats_mem(self,format1):

        parms = {"limit": 100, "sortOrder": f"{format1}"}
        link = self._link
        mem = sendreqwithparsm(link, parms)
        _lists = []
        if mem['data'] is None or mem['data'] == "null":
            return None
        try:
            return mem["data"][0].get("user", {}).get("username")

        except IndexError:
            return None

    @property
    def latest_member(self):
        _lists = self._stats_mem("Desc")
        return _lists

    @property
    def oldest_member(self):
        _lists = self._stats_mem("Asc")
        return _lists

    def _stats_games_private(self, format1):
        parms = {"accessFilter":"Private", "sortOrder": f"{format1}","limit": 100}
        link = self._link2
        mem = sendreqwithparsm(link, parms)
        if mem['data'] is None or mem['data'] == "null":
            return None
        try:
            return dict(name=mem["data"][0]["rootPlace"]["name"],id=mem["data"][0]["rootPlace"]["id"])
        except IndexError:
            return None

    def _stats_games_public(self, format1):
        parms = {"accessFilter": "Public", "sortOrder": f"{format1}", "limit": 100}
        link = self._link2
        mem = sendreqwithparsm(link, parms)
        if mem['data'] is None or mem['data'] == "null":
            return None
        try:
            return dict(name=mem["data"][0]["rootPlace"]["name"],id=mem["data"][0]["rootPlace"]["id"])
        except IndexError:
            return None

    def _stats_games(self, format1):
        parms = {"sortOrder": f"{format1}","limit": 100}
        link = self._link2
        mem = sendreqwithparsm(link, parms)
        print(mem["data"][0])

        if mem['data'] is None or mem['data'] == "null":
            return None
        try:
            return dict(name=mem["data"][0]["rootPlace"]["name"],id=mem["data"][0]["rootPlace"]["id"])
        except IndexError:
            return None

    @property
    def games(self):
        parms = {"sortOrder": "Asc", "limit": 100}
        link = self._link2
        gam = sendreqwithparsm(link, parms)
        _lists = []
        while True:
            for bill in gam['data']:
                pp = bill.get('name')
                _lists.append(pp)
            if gam["nextPageCursor"] is None or gam["nextPageCursor"] == "null":
                break
            payload = {'cursor': gam["nextPageCursor"], "limit": 100, "sortOrder": "Asc"}
            gam = sendreqwithparsm(link, payload)
        return _lists

    @property
    def private_games(self):
        parms = {"accessFilter":"Private", "sortOrder": "Asc","limit": 100}
        link = self._link2
        gam = sendreqwithparsm(link, parms)
        _lists = []
        while True:
            for bill in gam['data']:
                pp = bill.get('name')
                _lists.append(pp)
            if gam["nextPageCursor"] is None or gam["nextPageCursor"] == "null":
                break
            payload = {'cursor': gam["nextPageCursor"], "limit": 100, "sortOrder": "Asc"}
            gam = sendreqwithparsm(link, payload)
        return _lists

    @property
    def public_games(self):
        parms = {"accessFilter": "Public", "sortOrder": "Asc", "limit": 100}
        link = self._link2
        gam = sendreqwithparsm(link, parms)
        _lists = []
        while True:
            for bill in gam['data']:
                pp = bill.get('name')
                _lists.append(pp)
            if gam["nextPageCursor"] is None or gam["nextPageCursor"] == "null":
                break
            payload = {'cursor': gam["nextPageCursor"], "limit": 100, "sortOrder": "Asc"}
            gam = sendreqwithparsm(link, payload)
        return _lists

    @property
    def latest_game(self):
        _lists = self._stats_games("Desc")
        return _lists

    @property
    def oldest_game(self):
        _lists = self._stats_games("Asc")
        return _lists

    @property
    def latest_private_game(self):
        _lists = self._stats_games_private("Desc")
        return _lists

    @property
    def oldest_private_game(self):
        _lists = self._stats_games_private("Asc")
        return _lists

    @property
    def latest_public_game(self):
        _lists = self._stats_games_public("Desc")
        return _lists

    @property
    def oldest_public_game(self):
        _lists = self._stats_games_public("Asc")
        return _lists


class GroupSearch:
    def __init__(self,_name):
        self._name = _name
        self._eep = sendreq(f"https://groups.roblox.com/v1/groups/search/lookup?groupName={self._name}")

    @property
    def result(self):
        ok = self._eep
        _lis = []
        for data in ok["data"]:
            idd = data.get("id")
            name = data.get("name")
            e = dict(name=name,id=idd)
            _lis.append(e)
        return _lis

    def __repr__(self):
        return self.result