from .utils import send_request
import aiohttp
import datetime
import time
import asyncio
from .exceptions import GroupNotFound
from asyncinit import asyncinit
class GroupInfo:
    def __init__(self, groupID: int,smth):
        idkdd = isinstance(groupID, str)
        if idkdd:
            raise TypeError(f"{groupID} must be an integer")
        groupID = str(groupID).strip()
        self._ID = groupID
        if "name" not in smth.keys():
            raise GroupNotFound
        self._groupss = smth
        self._link = f"https://groups.roblox.com/v1/groups/{groupID}/users"
        self._link2 = f"https://games.roblox.com/v2/groups/{groupID}/games"


    @property
    async def allies(self):
        enimes = await send_request(f"https://api.roblox.com/groups/{self._ID}/allies")
        lala = enimes
        if lala["Groups"] is []:
            return None
        else:
            _lists = [dict(name=good.get("Name"),id=good.get('Id')) for good in lala['Groups']]
            return _lists

    @property
    async def enemies(self):
        enimes = await send_request(f"https://api.roblox.com/groups/{self._ID}/enemies")
        lala = enimes
        if lala["Groups"] is []:
            return None
        else:
            _lists = [dict(name=good.get("Name"),id=good.get('Id')) for good in lala['Groups']]
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
    def owner_id(self):
        return self._groupss["owner"]["userId"]
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
    async def thumbnail(self):
        dc = await send_request(f"https://www.roblox.com/group-thumbnails?params=%5B%7BgroupId:{self._ID}%7D%5D")
        return dc[0]["thumbnailUrl"]

    @property
    async def direct_url(self):
        dc = await send_request(f"https://www.roblox.com/group-thumbnails?params=%5B%7BgroupId:{self._ID}%7D%5D")
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
    async def members(self):
        link = self._link
        parms = {"limit": 100, "sortOrder": "Asc"}
        mem = await send_request(url=link,parms=parms)
        _lists = []
        while True:
            for bill in mem['data']:
                pp = bill.get("user", {}).get("username")
                #yield pp
                _lists.append(pp)

            if mem["nextPageCursor"] is None or mem["nextPageCursor"] == "null":
                break
            payload = {'cursor': mem["nextPageCursor"], "limit": 100, "sortOrder": "Asc"}
            mem = await send_request(link, parms=payload)
        return _lists

    async def _stats_mem(self,format1):

        parms = {"limit": 100, "sortOrder": f"{format1}"}
        link = self._link
        mem = await send_request(link, parms=parms)

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

    async def _stats_games_private(self, format1):
        parms = {"accessFilter":"Private", "sortOrder": f"{format1}","limit": 100}
        link = self._link2
        mem = await send_request(link, parms=parms)
        if mem['data'] is None or mem['data'] == "null":
            return None
        try:
            return dict(name=mem["data"][0]["name"],id=mem["data"][0]["id"])
        except IndexError:
            return None

    async def _stats_games_public(self, format1):
        parms = {"accessFilter": "Public", "sortOrder": f"{format1}", "limit": 100}
        link = self._link2
        mem = await send_request(link, parms=parms)
        if mem['data'] is None or mem['data'] == "null":
            return None
        try:
            return dict(name=mem["data"][0]["name"],id=mem["data"][0]["id"])
        except IndexError:
            return None

    async def _stats_games(self, format1):
        parms = {"sortOrder": f"{format1}","limit": 100}
        link = self._link2
        mem = await send_request(link, parms=parms)

        if mem['data'] is None or mem['data'] == "null":
            return None
        try:
            return dict(name=mem["data"][0]["rootPlace"]["name"],id=mem["data"][0]["rootPlace"]["id"])
        except IndexError:
            return None

    @property
    async def games(self):
        parms = {"sortOrder": "Asc", "limit": 100}
        link = self._link2
        gam = await send_request(link, parms=parms)
        _lists = []
        while True:
            for bill in gam['data']:
                pp = bill.get('name')
                iddd = bill.get('id')
                pp = dict(name=pp, id=iddd)
                _lists.append(pp)
            if gam["nextPageCursor"] is None or gam["nextPageCursor"] == "null":
                break
            payload = {'cursor': gam["nextPageCursor"], "limit": 100, "sortOrder": "Asc"}
            gam = await send_request(link, parms=payload)
        return _lists

    @property
    async def private_games(self):
        parms = {"accessFilter":"Private", "sortOrder": "Asc","limit": 100}
        link = self._link2
        gam = await send_request(link, parms=parms)
        _lists = []
        while True:
            for bill in gam['data']:
                pp = bill.get('name')
                iddd = bill.get('id')
                pp = dict(name=pp,id=iddd)
                _lists.append(pp)
            if gam["nextPageCursor"] is None or gam["nextPageCursor"] == "null":
                break
            payload = {'cursor': gam["nextPageCursor"], "limit": 100, "sortOrder": "Asc"}
            gam = await send_request(link, parms=payload)
        return _lists

    @property
    async def public_games(self):
        parms = {"accessFilter": "Public", "sortOrder": "Asc", "limit": 100}
        link = self._link2
        gam = await send_request(link, parms=parms)
        _lists = []
        while True:
            for bill in gam['data']:
                pp = bill.get('name')
                iddd = bill.get('id')
                pp = dict(name=pp, id=iddd)
                _lists.append(pp)
            if gam["nextPageCursor"] is None or gam["nextPageCursor"] == "null":
                break
            payload = {'cursor': gam["nextPageCursor"], "limit": 100, "sortOrder": "Asc"}
            gam = await send_request(link, parms=payload)
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