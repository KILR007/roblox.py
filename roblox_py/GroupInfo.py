from .exceptions import GroupNotFound
from .Classes import PartialInfo
from .utils import Requests


class GroupInfo:
    """

    Represents a ROBLOX Group.

    """

    def __init__(self, request: Requests, groupID: int):
        """

        Represents a ROBLOX Group.

        **Parameters**
        --------------
        request : roblox_py.Requests
            Requests Class to do HTTP Requests
        groupID : int
            Group ID


        """
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
        """
        Must be called before using the class else the class will misbehave.
        """
        eee = await self.request.request(url=f"https://groups.roblox.com/v1/groups/{self._ID}", method='get')
        if "name" not in eee.keys():
            raise GroupNotFound
        self._groupss = eee

    async def allies_count(self) -> int:
        """
        Gets the Group allies count
        """
        if self._allies is None:
            self._allies = await self.request.request(
                url=f"https://groups.roblox.com/v1/groups/{self._ID}/relationships/allies?"
                    f"model.startRowIndex=0&model.maxRows=1",
                method='get')
        lala = self._allies
        return lala['totalGroupCount']

    async def enemies_count(self) -> int:
        """
        Gets the Group enemies  count
        """
        if self._enemies is None:
            self._enemies = await self.request.request(
                url=f"https://groups.roblox.com/v1/groups/{self._ID}/relationships/enemies?"
                    f"model.startRowIndex=0&model.maxRows=1",
                method='get')
        lala = self._enemies
        return lala['totalGroupCount']

    async def allies(self):
        """
        Gets the Group allies
        """
        if self._allies is None:
            self._allies = await self.request.request(
                url=f"https://groups.roblox.com/v1/groups/{self._ID}/relationships/allies?"
                    f"model.startRowIndex=0&model.maxRows=1",
                method='get')
        lala = self._allies
        if lala["relatedGroups"] is []:
            return None
        else:
            _lists = [
                PartialInfo(
                    name=good.get("name"),
                    id=good.get('id')) for good in lala['relatedGroups']]
            return _lists

    async def enemies(self):
        """
        Gets the Group enemies
        """
        if self._enemies is None:
            self._enemies = await self.request.request(
                url=f"https://groups.roblox.com/v1/groups/{self._ID}/relationships/enemies?"
                    f"model.startRowIndex=0&model.maxRows=1",
                method='get')
        lala = self._enemies
        if lala["relatedGroups"] is []:
            return None
        else:
            _lists = [
                PartialInfo(
                    name=good.get("name"),
                    id=good.get('id')) for good in lala['relatedGroups']]
            return _lists

    @property
    def name(self) -> str:
        """
        Gets the Groups Name
        """
        return self._groupss["name"]

    def __repr__(self):
        return self.name

    @property
    def id(self) -> int:
        """
        Gets the Groups ID
        """
        return self._groupss["id"]

    @property
    def owner(self) -> PartialInfo:
        """
        Returns of the group
        """
        return PartialInfo(
            name=self._groupss["owner"]["username"],
            id=self._groupss["owner"]["userId"])

    @property
    def member_count(self) -> int:
        """
        Returns the member Count
        """
        return self._groupss["memberCount"]

    @property
    def is_private(self) -> bool:
        """
        Check if the group is private or not
        """
        if self._groupss["publicEntryAllowed"] is True:
            return False
        else:
            return True

    @property
    def is_premium_only_entry(self):
        return self._groupss["isBuildersClubOnly"]

    @property
    def shout(self):
        """
        Check if the group is private or not
        """
        try:
            if self._groupss["shout"]["body"] == "":
                return None
            else:
                return self._groupss["shout"]["body"]
        except TypeError:
            return None

    @property
    def shout_poster(self):
        """
        Returns shout poster
        """

        try:
            if self._groupss["shout"]["body"] == "":
                return None
            else:
                return PartialInfo(
                    name=self._groupss["shout"]["poster"]["username"],
                    id=self._groupss["shout"]["poster"]["userId"])
        except TypeError:
            return None

    async def thumbnail(self) -> str:
        """
        Gets the group thumbnail image link
        """
        dc = await self.request.request(
            url=f"https://www.roblox.com/group-thumbnails?params=%5B%7BgroupId:{self._ID}%7D%5D", method='get')
        return dc[0]["thumbnailUrl"]

    @property
    def direct_url(self) -> str:
        """
        Returns Roblox URL to the bundle
        """
        return f'https://www.roblox.com/groups/group.aspx?gid={self._ID}'

    @property
    def description(self):
        """
        Gets Group Description
        """
        try:
            if self._groupss["description"] == "":
                return None
            else:
                return self._groupss["description"]
        except TypeError:
            return None

    async def members(self) -> list:
        """
        Returns a list of Group Members
        """
        link = self._link
        parms = {"limit": 100, "sortOrder": "Asc"}
        mem = await self.request.request(url=link, parms=parms)
        _lists = []
        while True:
            for bill in mem['data']:
                pp = bill.get("user", {}).get("username")
                pp1 = bill.get('user', {}).get('userId')
                _lists.append(PartialInfo(id=pp1, name=pp))

            if mem["nextPageCursor"] is None or mem["nextPageCursor"] == "null":
                break
            payload = {
                'cursor': mem["nextPageCursor"],
                "limit": 100,
                "sortOrder": "Asc"}
            mem = await self.request.request(link, parms=payload)
        return _lists

    async def _stats_mem(self, format1):
        """
        Function Used by roblox_py.GroupInfo.latest_member & roblox_py.GroupInfo.oldest_member
        """
        parms = {"limit": 100, "sortOrder": f"{format1}"}
        link = self._link
        mem = await self.request.request(link, parms=parms)

        _lists = []
        if mem['data'] is None or mem['data'] == "null":
            return None
        try:
            return PartialInfo(
                id=mem["data"][0].get(
                    "user", {}).get("userId"), name=mem["data"][0].get(
                    "user", {}).get("username"))

        except IndexError:
            return None

    async def newest_member(self):
        """
        Gets the newest Member of the group
        """
        _lists = await self._stats_mem("Desc")
        return _lists

    async def oldest_member(self):
        """
        Gets the oldest Member of the group
        """
        _lists = await self._stats_mem("Asc")
        return _lists

    async def _stats_games_private(self, format1):
        parms = {
            "accessFilter": "Private",
            "sortOrder": f"{format1}",
            "limit": 100}
        link = self._link2
        mem = await self.request.request(link, parms=parms)
        if mem['data'] is None or mem['data'] == "null":
            return None
        try:
            return PartialInfo(
                name=mem["data"][0]["name"],
                id=mem["data"][0]["rootPlace"]["id"])
        except IndexError:
            return None

    async def _stats_games_public(self, format1):
        parms = {
            "accessFilter": "Public",
            "sortOrder": f"{format1}",
            "limit": 100}
        link = self._link2
        mem = await self.request.request(link, parms=parms)
        if mem['data'] is None or mem['data'] == "null":
            return None
        try:
            return PartialInfo(
                name=mem["data"][0]["name"],
                id=mem["data"][0]["rootPlace"]["id"])
        except IndexError:
            return None

    async def _stats_games(self, format1):
        parms = {"sortOrder": f"{format1}", "limit": 100}
        link = self._link2
        mem = await self.request.request(url=link, parms=parms)

        if mem['data'] is None or mem['data'] == "null":
            return None
        try:
            return PartialInfo(
                name=mem["data"][0]["name"],
                id=mem["data"][0]["rootPlace"]["id"])
        except IndexError:
            return None

    async def games(self) -> list:
        """
        Returns all game of the group
        """
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
            payload = {
                'cursor': gam["nextPageCursor"],
                "limit": 100,
                "sortOrder": "Asc"}
            gam = await self.request.request(link, parms=payload)
        return _lists

    async def private_games(self) -> list:
        """
        Returns all private game of the group
        """
        parms = {"accessFilter": "Private", "sortOrder": "Asc", "limit": 100}
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
            payload = {
                'cursor': gam["nextPageCursor"],
                "limit": 100,
                "sortOrder": "Asc"}
            gam = await self.request.request(url=link, parms=payload)
        return _lists

    async def public_games(self) -> list:
        """
        Returns all public game of the group
        """
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
            payload = {
                'cursor': gam["nextPageCursor"],
                "limit": 100,
                "sortOrder": "Asc"}
            gam = await self.request.request(url=link, parms=payload)
        return _lists

    async def newest_game(self):
        """
        Returns the newest game of the group(not limited to public/private)
        """
        _lists = await self._stats_games("Desc")
        return _lists

    async def oldest_game(self):
        """
        Returns the oldest game of the group(not limited to public/private)
        """
        _lists = await self._stats_games("Asc")
        return _lists

    async def newest_private_game(self):
        """
        Returns the newest private game of the group
        """
        _lists = await self._stats_games_private("Desc")
        return _lists

    async def oldest_private_game(self):
        """
        Returns the oldest private game of the group
        """
        _lists = await self._stats_games_private("Asc")
        return _lists

    async def newest_public_game(self):
        """
        Returns the newest public game of the group
        """
        _lists = await self._stats_games_public("Desc")
        return _lists

    async def oldest_public_game(self):
        """
        Returns the oldest public game of the group
        """
        _lists = await self._stats_games_public("Asc")
        return _lists

    async def get_users_in_role(self, role_id: int) -> list:
        """
        Gets users in a specific role
        """
        link = f"https://groups.roblox.com/v1/groups/{self._ID}/roles/{role_id}/users"
        parm = {"sortOrder": "Asc", "limit": 100}
        res = await self.request.request(url=link, method='get', parms=parm)
        _list = []
        while True:
            for info in res['data']:
                username = info.get('username')
                user_id = info.get('userId')
                inst = PartialInfo(name=username, id=user_id)
                _list.append(inst)
            if res["nextPageCursor"] is None or res["nextPageCursor"] == "null":
                break
            payload = {
                "limit": 100,
                "sortOrder": "Asc",
                'cursor': res["nextPageCursor"]}
            res = await self.request.request(url=link, method='get', parms=payload)
        return _list

    async def get_roles_info(self) -> list:
        """
        Gives list of roles in the group
        """
        link = f"https://groups.roblox.com/v1/groups/{self._ID}/roles"
        res = await self.request.request(url=link, method='get')
        _list = []
        for stuff in res['roles']:
            name = stuff.get('name')
            role_id = stuff.get('id')
            inst = PartialInfo(name=name, id=role_id)
            _list.append(inst)
        return _list
