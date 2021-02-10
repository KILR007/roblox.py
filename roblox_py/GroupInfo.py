from .exceptions import GroupNotFound
from .Classes import PartialInfo
class GroupInfo:
    def __init__(self, request,groupID: int):
        self.request = request
        idkdd = isinstance(groupID, str)
        if idkdd:
            raise TypeError(f"{groupID} must be an integer")
        groupID = str(groupID).strip()
        self._ID = groupID
        self._allies = None
        self._enemies = None
        self._groupss = None
        self._link = f"https://groups.roblox.com/v1/groups/{groupID}/users"
        self._link2 = f"https://games.roblox.com/v2/groups/{groupID}/games"
    async def update(self):
        eee = await self.request.request(url=f"https://groups.roblox.com/v1/groups/{self._ID}",method='get')
        if "name" not in eee.keys():
            raise GroupNotFound
        self._groupss  = eee


    async def allies_count(self):
        if self._allies is None:
            self._allies = await self.request.request(url=f"https://groups.roblox.com/v1/groups/{self._ID}/relationships/allies?model.startRowIndex=0&model.maxRows=1",method='get')
        lala = self._allies
        return lala['totalGroupCount']

    async def enemies_count(self):
        if self._enemies is None:
            self._enemies = await self.request.request(url=f"https://groups.roblox.com/v1/groups/{self._ID}/relationships/enemies?model.startRowIndex=0&model.maxRows=1",method='get')
        lala = self._enemies
        return lala['totalGroupCount']

    async def allies(self):
        if self._allies is None:
            self._allies = await self.request.request(url=f"https://groups.roblox.com/v1/groups/{self._ID}/relationships/allies?model.startRowIndex=0&model.maxRows=1",method='get')
        lala = self._allies
        if lala["relatedGroups"] is []:
            return None
        else:
            _lists = [PartialInfo(name=good.get("name"),id=good.get('id')) for good in lala['relatedGroups']]
            return _lists

    async def enemies(self):
         if self._enemies is None:
            self._enemies = await self.request.request(url=f"https://groups.roblox.com/v1/groups/{self._ID}/relationships/enemies?model.startRowIndex=0&model.maxRows=1",method='get')
        lala = self._enemies
        if lala["relatedGroups"] is []:
            return None
        else:
            _lists = [PartialInfo(name=good.get("name"),id=good.get('id')) for good in lala['relatedGroups']]
            return _lists

    @property
    def name(self):
        return self._groupss["name"]


    def __str__(self):
        return self.name

    @property
    def id(self):
        return self._groupss["id"]

    @property
    def owner(self):
        return PartialInfo(name=self._groupss["owner"]["username"],id=self._groupss["owner"]["userId"])


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
                return PartialInfo(name=self._groupss["shout"]["poster"]["username"],
                                  id=self._groupss["shout"]["poster"]["userId"])
        except TypeError:
            return None

    async def thumbnail(self):
        dc = await self.request.request(url=f"https://www.roblox.com/group-thumbnails?params=%5B%7BgroupId:{self._ID}%7D%5D",method='get')
        return dc[0]["thumbnailUrl"]

    @property
    async def direct_url(self):
        return f'https://www.roblox.com/groups/group.aspx?gid={self._ID}'
    @property
    def description(self):
        try:
            if self._groupss["description"] == "":
                return None
            else:
                return self._groupss["description"]
        except TypeError:
            return None

    async def members(self):
        link = self._link
        parms = {"limit": 100, "sortOrder": "Asc"}
        mem = await self.request.request(url=link,parms=parms)
        _lists = []
        while True:
            for bill in mem['data']:
                pp = bill.get("user", {}).get("username")
                pp1 = bill.get('user',{}).get('userId')
                _lists.append(PartialInfo(id=pp1,name=pp))

            if mem["nextPageCursor"] is None or mem["nextPageCursor"] == "null":
                break
            payload = {'cursor': mem["nextPageCursor"], "limit": 100, "sortOrder": "Asc"}
            mem = await self.request.request(link, parms=payload)
        return _lists

    async def _stats_mem(self,format1):

        parms = {"limit": 100, "sortOrder": f"{format1}"}
        link = self._link
        mem = await self.request.request(link, parms=parms)

        _lists = []
        if mem['data'] is None or mem['data'] == "null":
            return None
        try:
            return PartialInfo(id=mem["data"][0].get("user", {}).get("userId"),name=mem["data"][0].get("user", {}).get("username"))

        except IndexError:
            return None

    async def latest_member(self):
        _lists = await self._stats_mem("Desc")
        return _lists

    async def oldest_member(self):
        _lists = await self._stats_mem("Asc")
        return _lists

    async def _stats_games_private(self, format1):
        parms = {"accessFilter":"Private", "sortOrder": f"{format1}","limit": 100}
        link = self._link2
        mem = await self.request.request(link, parms=parms)
        if mem['data'] is None or mem['data'] == "null":
            return None
        try:
            return PartialInfo(name=mem["data"][0]["name"],id=mem["data"][0]["rootPlace"]["id"])
        except IndexError:
            return None

    async def _stats_games_public(self, format1):
        parms = {"accessFilter":"Public", "sortOrder": f"{format1}","limit": 100}
        link = self._link2
        mem = await self.request.request(link, parms=parms)
        if mem['data'] is None or mem['data'] == "null":
            return None
        try:
            return PartialInfo(name=mem["data"][0]["name"], id=mem["data"][0]["rootPlace"]["id"])
        except IndexError:
            return None

    async def _stats_games(self, format1):
        parms = {"sortOrder": f"{format1}","limit": 100}
        link = self._link2
        mem = await self.request.request(url=link, parms=parms)

        if mem['data'] is None or mem['data'] == "null":
            return None
        try:
            return PartialInfo(name=mem["data"][0]["name"],id=mem["data"][0]["rootPlace"]["id"])
        except IndexError:
            return None

    async def games(self):
        parms = {"sortOrder": "Asc", "limit": 100}
        link = self._link2
        gam = await self.request.request(url=link, parms=parms)
        _lists = []
        while True:
            for bill in gam['data']:
                pp = bill.get('name')
                iddd = bill["rootPlace"].get('id')

                pp = PartialInfo(name=pp, id=iddd)
                _lists.append(pp)
            if gam["nextPageCursor"] is None or gam["nextPageCursor"] == "null":
                break
            payload = {'cursor': gam["nextPageCursor"], "limit": 100, "sortOrder": "Asc"}
            gam = await self.request.request(link, parms=payload)
        return _lists

    async def private_games(self):
        parms = {"accessFilter":"Private", "sortOrder": "Asc","limit": 100}
        link = self._link2
        gam = await self.request.request(url=link, parms=parms)
        _lists = []
        while True:
            for bill in gam['data']:
                pp = bill.get('name')
                iddd = bill["rootPlace"].get('id')
                pp = PartialInfo(name=pp,id=iddd)
                _lists.append(pp)
            if gam["nextPageCursor"] is None or gam["nextPageCursor"] == "null":
                break
            payload = {'cursor': gam["nextPageCursor"], "limit": 100, "sortOrder": "Asc"}
            gam = await self.request.request(url=link, parms=payload)
        return _lists

    async def public_games(self):
        parms = {"accessFilter": "Public", "sortOrder": "Asc", "limit": 100}
        link = self._link2
        gam = await self.request.request(url=link, parms=parms)
        _lists = []
        while True:
            for bill in gam['data']:
                pp = bill.get('name')
                iddd = bill["rootPlace"].get('id')
                pp = PartialInfo(name=pp, id=iddd)
                _lists.append(pp)
            if gam["nextPageCursor"] is None or gam["nextPageCursor"] == "null":
                break
            payload = {'cursor': gam["nextPageCursor"], "limit": 100, "sortOrder": "Asc"}
            gam = await self.request.request(url=link, parms=payload)
        return _lists

    async def latest_game(self):
        _lists = await self._stats_games("Desc")
        return _lists

    async def oldest_game(self):
        _lists = await self._stats_games("Asc")
        return _lists

    async def latest_private_game(self):
        _lists = await self._stats_games_private("Desc")
        return _lists

    async def oldest_private_game(self):
        _lists = await self._stats_games_private("Asc")
        return _lists

    async def latest_public_game(self):
        _lists = await self._stats_games_public("Desc")
        return _lists

    async def oldest_public_game(self):
        _lists = await self._stats_games_public("Asc")
        return _lists
