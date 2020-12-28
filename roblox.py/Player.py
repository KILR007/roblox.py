from .utils import send_request
import aiohttp
import datetime
import time
import asyncio
from .exceptions import PlayerNotFound
from asyncinit import asyncinit
class PlayerInfo:

    def __init__(self, playerID: int,alr):
        idkdd = isinstance(playerID, str)
        if idkdd:
            raise TypeError(f"{playerID} must be an integer")
        if "id" not in alr.keys():
            raise PlayerNotFound
        self._Id = playerID
        self.ID = playerID
        self._dat = playerID
        self._Ascsss = alr
        self._friends = None
        self._following = None
        self._badges = None
        self._groups = None
        self._follower = None

    @property
    async def friends(self):

        if not self._friends:

            _count = await send_request(f"https://friends.roblox.com/v1/users/{self.ID}/friends/count")
            _friendship = await send_request(f"https://friends.roblox.com/v1/users/{self.ID}/friends")
            e = Friends(self._dat,_friendship,_count)
            return e

        return None
    @property
    async def following(self):
        if not self._following:
            parms = {"limit": 100, "sortOrder": "Asc"}
            _link = f"https://friends.roblox.com/v1/users/{self._dat}/followings"
            _stuff = await send_request(_link, parms=parms)
            _count = await send_request(f"https://friends.roblox.com/v1/users/{self._dat}/followings/count")
            e = Following(self._dat, stuff=_stuff, count=_count)
            return e

        return None

    @property
    async def badges(self):
        if not self._badges:
            yeah = await send_request(f"https://www.roblox.com/badges/roblox?userId={self._dat}")

            e = Badges(self._dat,yeah)
            return e

        return None

    @property
    async def groups(self):
        if not self._groups:
            _groups = await send_request(f"https://api.roblox.com/users/{self._dat}/groups")
            e = Groups(self._dat,_groups)
            return e

        return None



    @property
    async def followers(self):

        if not self._follower:
            parms = {"limit": 100, "sortOrder": "Asc"}

            _link = f"https://friends.roblox.com/v1/users/{self._dat}/followers"
            _stuff = await send_request(_link, parms=parms)
            _count = await send_request(f"https://friends.roblox.com/v1/users/{self._dat}/followers/count")
            e = Follower(self._dat,link1=_stuff,link2=_count)
            return e

        return None

    @property
    async def game(self):
        return Game(user_id=self._dat)
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
    async def avatar(self):
        p = {
            "size" : "720x720",
            "format" : "Png",
        }
        noob = await send_request(f"https://thumbnails.roblox.com/v1/users/avatar?userIds={self._dat}",parms=p)
        return noob["data"][0]["imageUrl"]

    @property
    async def thumbnail(self):
        f = self._dat
        noob = await send_request(f"https://www.roblox.com/headshot-thumbnail/json?userId={f}&width=180&height=180")
        return noob['Url']

    @property
    async def promotion_channel(self):
        f = self._dat
        e = await send_request(url=f'https://accountinformation.roblox.com/v1/users/{f}/promotion-channels')
        return e



















class Game:
    def __init__(self,user_id):
        self._dat = user_id

    @property
    async def get_private_games(self):
        payload = {'sortOrder': "Asc", "limit": 100}
        link = f"https://games.roblox.com/v2/users/{self._dat}/games?accessFilter=Private"
        stuff = await send_request(url=link, parms=payload)
        _lists = []

        while True:
            for bill in stuff['data']:
                pp = bill.get('name')
                pp1 = bill.get("id")
                _lists.append(dict(name=pp, id=pp1))
            if stuff["nextPageCursor"] is None or stuff["nextPageCursor"] == "null":
                break
            payload = {'cursor': stuff["nextPageCursor"], "limit": 100, "sortOrder": "Asc"}
            stuff = await send_request(url=link, parms=payload)
        return _lists

    async def _stats_games(self, format1):
        parms = {"limit": 100, "sortOrder": f"{format1}"}
        link = f"https://games.roblox.com/v2/users/{self._dat}/games?accessFilter=Private"
        stuff = await send_request(url=link, parms=parms)
        _lists = []
        if stuff['data'] is None or stuff['data'] == "null":
            return None
        try:
            return dict(name=stuff['data'][0]["name"], id=stuff['data'][0]["id"])
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

class Friends:
    def __init__(self,id,frienship,count):

        self.ID = id
        self._friendship = frienship
        self._count = count

    @property
    def name(self):
        f = self._friendship
        _lists = [bill.get('name')  for bill in f["data"]]
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
    def __repr__(self):
        return self.name



class Following:
    def __init__(self, id,stuff,count):
        self._dat = id
        parms = {"limit": 100, "sortOrder": "Asc"}

        self._link = f"https://friends.roblox.com/v1/users/{self._dat}/followings"
        self._stuff = stuff
        self._count = count

    async def _stats(self, format1):
        parms = {"limit": 100, "sortOrder": f"{format1}"}
        link = self._link
        stuff = await send_request(link, parms=parms)
        _lists = []
        if stuff['data'] is None or stuff['data'] == "null":
            return None
        try:
            return stuff['data'][0]["name"]
        except IndexError:
            return None

    @property
    async def name(self):
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
            stuff = await send_request(link, parms=payload)
        return _lists

    @property
    async def latest(self):
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
        pass

    def __repr__(self):
        return self.name
class Groups:
    def __init__(self,id,ok):
        self._dat = id
        self._groups = ok

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

    def __repr__(self):
        return self.name
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
    async def primary_group(self):
        ok = await send_request(f"https://groups.roblox.com/v1/users/{self._dat}/groups/primary/role")

        try:
            return dict(name=ok["group"]["name"], id=ok["group"]["id"])
        except KeyError:
            return None
class Badges:
    def __init__(self,ID,badge):
        self._dat = ID
        self._badges = badge
    @property
    def roblox_badges(self):
        mm = self._badges
        _lists = [item["Name"] for item in mm["RobloxBadges"]]
        return _lists

    async def _stats(self,format1):
        f = self._dat
        parms = {"limit": 100, "sortOrder": f"{format1}"}
        link = f"https://badges.roblox.com/v1/users/{f}/badges"
        stuff = await send_request(link, parms=parms)
        _lists = []
        if stuff['data'] is None or stuff['data'] == "null":
            return None
        try:
            return stuff['data'][0]["name"]
        except IndexError:
            return None

    @property
    async def badges(self):
        f = self._dat
        parms = {"limit": 100, "sortOrder": "Asc"}
        link = f"https://badges.roblox.com/v1/users/{f}/badges"

        stuff = await send_request(link, parms=parms)
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
            stuff = await send_request(link, parms=payload)
        return _lists

    @property
    def count_badges(self):
        return len(self._badges) if not None else 0

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


class Follower:
    def __init__(self,ID,link1,link2):
        self._dat = ID

        self._link = f"https://friends.roblox.com/v1/users/{self._dat}/followers"
        self._stuff = link1
        self._count = link2

   
    async def _stats(self, format1):
        parms = {"limit": 100, "sortOrder": f"{format1}"}
        link = self._link
        stuff = await send_request(link, parms=parms)
        _lists = []
        if stuff['data'] is None or stuff['data'] == "null":
            return None
        try:
            return stuff['data'][0]["name"]
        except IndexError:
            return None

    @property
    async def name(self):
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
            stuff = await send_request(link, parms=payload)
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
            return None

    @property
    def count(self):
        return self._count["count"]


