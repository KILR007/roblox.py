import datetime
from .exceptions import PlayerNotFound


class PlayerInfo:

    def __init__(self, request,playerID: int):
        self.request = request
        idkdd = isinstance(playerID, str)
        if idkdd:
            raise TypeError(f"{playerID} must be an integer")
        self._Id = playerID
        self._Ascsss = None
        self._following = None
        self._badges = None
        self._groups = None
        self._follower = None
        self._friendship = None
        self._stuff_following = None
        self._stuff_follower = None

    async def update(self):
        xd = await self.request.request(url=f"https://users.roblox.com/v1/users/{self._Id}",method='get')
        if "id" not in xd.keys():
            raise PlayerNotFound
        self._Ascsss = xd






    @property
    def name(self):
        return self._Ascsss["name"]

    def __repr__(self):
        return self.name

    @property
    def id(self):
        return self._Id

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
        f = self._Id
        return f"https://www.roblox.com/users/{f}/profile"

    async def avatar(self):
        p = {
            "size" : "720x720",
            "format" : "Png",
        }
        noob = await self.request.request(url=f"https://thumbnails.roblox.com/v1/users/avatar?userIds={self._Id}",parms=p)
        return noob["data"][0]["imageUrl"]

    async def thumbnail(self):
        f = self._Id
        noob = await self.request.request(url=f"https://www.roblox.com/headshot-thumbnail/json?userId={f}&width=180&height=180")
        return noob['Url']


    async def promotion_channel(self):
        f = self._Id
        e = await self.request.request(url=f'https://accountinformation.roblox.com/v1/users/{f}/promotion-channels')
        return e


    async def get_public_games(self):
        payload = {'sortOrder': "Asc", "limit": 100}
        link = f"https://games.roblox.com/v2/users/{self._Id}/games?accessFilter=Public"
        stuff = await self.request.request(url=link, parms=payload)
        _lists = []

        while True:
            for bill in stuff['data']:
                pp = bill.get('name')
                pp1 = bill.get("id")
                _lists.append(dict(name=pp, id=pp1))
            if stuff["nextPageCursor"] is None or stuff["nextPageCursor"] == "null":
                break
            payload = {'cursor': stuff["nextPageCursor"], "limit": 100, "sortOrder": "Asc"}
            stuff = await self.request.request(url=link, parms=payload)
        return _lists
    async def _stats_games_public(self, format1):
        parms = {"limit": 100, "sortOrder": f"{format1}"}
        link = f"https://games.roblox.com/v2/users/{self._Id}/games?accessFilter=Public"
        stuff = await self.request.request(url=link, parms=parms)
        _lists = []
        if stuff['data'] is None or stuff['data'] == "null":
            return None
        try:
            return dict(name=stuff['data'][0]["name"], id=stuff['data'][0]["id"])
        except IndexError:
            return None


    async def oldest_public_game(self):
        _lists = await self._stats_games_public("Asc")
        try:
            return _lists
        except IndexError:
            return


    async def latest_public_game(self):
        _lists = await self._stats_games_public("Desc")
        try:
            return _lists
        except IndexError:
            return

    async def get_private_games(self):
        payload = {'sortOrder': "Asc", "limit": 100}
        link = f"https://games.roblox.com/v2/users/{self._Id}/games?accessFilter=Private"
        stuff = await self.request.request(url=link, parms=payload)
        _lists = []

        while True:
            for bill in stuff['data']:
                pp = bill.get('name')
                pp1 = bill.get("id")
                _lists.append(dict(name=pp, id=pp1))
            if stuff["nextPageCursor"] is None or stuff["nextPageCursor"] == "null":
                break
            payload = {'cursor': stuff["nextPageCursor"], "limit": 100, "sortOrder": "Asc"}
            stuff = await self.request.request(url=link, parms=payload)
        return _lists

    async def _stats_games(self, format1):
        parms = {"limit": 100, "sortOrder": f"{format1}"}
        link = f"https://games.roblox.com/v2/users/{self._Id}/games?accessFilter=Private"
        stuff = await self.request.request(url=link, parms=parms)
        _lists = []
        if stuff['data'] is None or stuff['data'] == "null":
            return None
        try:
            return dict(name=stuff['data'][0]["name"], id=stuff['data'][0]["id"])
        except IndexError:
            return None


    async def oldest_private_game(self):
        _lists = await self._stats_games("Asc")
        try:
            return _lists
        except IndexError:
            return


    async def latest_private_game(self):
        _lists = await self._stats_games("Desc")
        try:
            return _lists
        except IndexError:
            return






    async def friends(self):
        if self._friendship is None:
            self._friendship = await self.request.request(url=f"https://friends.roblox.com/v1/users/{self._Id}/friends")
        _lists = [bill.get('name') for bill in self._friendship["data"]]
        return _lists


    async def newest_friend(self):
        try:
            if self._friendship is None:
                self._friendship = await self.request.request(url=f"https://friends.roblox.com/v1/users/{self._Id}/friends")

            return self._friendship["data"][0]["name"]
        except IndexError:
            return None


    async def friends_count(self):
        ff = await self.request.request(url=f"https://friends.roblox.com/v1/users/{self._Id}/friends/count")
        return ff["count"]

    async def oldest_friend(self):
        if self._friendship is None:
            self._friendship = await self.request.request(url=f"https://friends.roblox.com/v1/users/{self._Id}/friends")
        f = self._friendship
        if len(f["data"]) == 0:
            return None
        else:
            D = len(f["data"]) - 1
            return f["data"][D]["name"]




    async def _stats_following(self, format1):
        parms = {"limit": 100, "sortOrder": f"{format1}"}
        link = f"https://friends.roblox.com/v1/users/{self._Id}/followings"
        stuff = await self.request.request(link, parms=parms)
        _lists = []
        if stuff['data'] is None or stuff['data'] == "null":
            return None
        try:
            return stuff['data'][0]["name"]
        except IndexError:
            return None


    async def following(self):
        if self._stuff_following is None:
            parms = {"limit": 100, "sortOrder": "Asc"}
            self._stuff_following = await self.request.request(
                url=f"https://friends.roblox.com/v1/users/{self._Id}/followings", parms=parms)

        link = f"https://friends.roblox.com/v1/users/{self._Id}/followings"
        stuff = self._stuff_following
        _lists = []

        while True:
            for bill in stuff['data']:
                pp = bill.get('name')
                _lists.append(pp)
            if stuff["nextPageCursor"] is None or stuff["nextPageCursor"] == "null":
                break
            payload = {'cursor': stuff["nextPageCursor"], "limit": 100, "sortOrder": "Asc"}
            stuff = await self.request.request(link, parms=payload)
        return _lists

    async def newest_following(self):
        _lists = await self._stats_following("Desc")
        if _lists is None:
            return None
        try:
            return _lists
        except IndexError:
            return

    async def oldest_following(self):
        _lists = await self._stats_following("Asc")
        if _lists is None:
            return None
        try:
            return _lists
        except IndexError:
            return
    async def following_count(self):

        _count = await self.request.request(url=f"https://friends.roblox.com/v1/users/{self._Id}/followings/count")
        return _count["count"]

    async def groups(self):
        if self._groups is None:
            self._groups = await self.request.request(url=f"https://api.roblox.com/users/{self._Id}/groups")

        f = self._groups
        _lists = [bill.get('Name') for bill in f]
        if _lists is []:
            return None
        return _lists

    async def newest_group(self):
        if self._groups is None:
            self._groups = await self.request.request(url=f"https://api.roblox.com/users/{self._Id}/groups")
        f = self._groups

        try:
            return f[0]["Name"]
        except IndexError:
            return None

    async def oldest_group(self):
        if self._groups is None:
            self._groups = await self.request.request(url=f"https://api.roblox.com/users/{self._Id}/groups")

        n = self._groups
        if len(n) == 0:
            return None
        else:
            D = len(n) - 1
            return n[D]["Name"]

    async def group_count(self):
        if self._groups is None:
            self._groups = await self.request.request(url=f"https://api.roblox.com/users/{self._Id}/groups")
        if len(self._groups) == 0:
            return 0
        else:
            return len(self._groups)

    async def primary_group(self):
        ok = await self.request.request(f"https://groups.roblox.com/v1/users/{self._Id}/groups/primary/role")

        try:
            return dict(name=ok["group"]["name"], id=ok["group"]["id"])
        except KeyError:
            return None

    async def roblox_badges(self):
        if self._badges is None:
            self._badges = await self.request.request(url=f"https://www.roblox.com/badges/roblox?userId={self._Id}")
        mm = self._badges

        _lists = [item["Name"] for item in mm["RobloxBadges"]]
        return _lists

    async def _stats_badge(self,format1):
        f = self._Id
        parms = {"limit": 100, "sortOrder": f"{format1}"}
        link = f"https://badges.roblox.com/v1/users/{f}/badges"
        stuff = await self.request.request(link, parms=parms)
        _lists = []
        if stuff['data'] is None or stuff['data'] == "null":
            return None
        try:
            return stuff['data'][0]["name"]
        except IndexError:
            return None

    async def badges(self):
        f = self._Id
        parms = {"limit": 100, "sortOrder": "Asc"}
        link = f"https://badges.roblox.com/v1/users/{f}/badges"

        stuff = await self.request.request(link, parms=parms)
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
            stuff = await self.request.request(link, parms=payload)
        return _lists

    async def count_roblox_badges(self):
        if self._badges is None:
            self._badges = await self.request.request(url=f"https://www.roblox.com/badges/roblox?userId={self._Id}")
        return len(self._badges) if not None else 0

    async def latest_badge(self):
        _lists = await self._stats_badge("Desc")
        if _lists is None:
            return None
        try:
            return _lists
        except IndexError:
            return

    async def oldest_badge(self):
        _lists = await self._stats_badge("Asc")
        if _lists is None:
            return None
        try:
            return _lists
        except IndexError:
            return

    async def _stats_follower(self, format1):
        parms = {"limit": 100, "sortOrder": f"{format1}"}
        link = f"https://friends.roblox.com/v1/users/{self._Id}/followers"
        stuff = await self.request.request(link, parms=parms)
        _lists = []
        if stuff['data'] is None or stuff['data'] == "null":
            return None
        try:
            return stuff['data'][0]["name"]
        except IndexError:
            return None

    async def followers(self):
        if self._stuff_follower is None:
            parms = {"limit": 100, "sortOrder": "Asc"}
            self._stuff_follower = await self.request.request(
                url=f"https://friends.roblox.com/v1/users/{self._Id}/followers", parms=parms)

        link = f"https://friends.roblox.com/v1/users/{self._Id}/followers"
        stuff = self._stuff_following
        _lists = []

        while True:
            for bill in stuff['data']:
                pp = bill.get('name')
                _lists.append(pp)
            if stuff["nextPageCursor"] is None or stuff["nextPageCursor"] == "null":
                break
            payload = {'cursor': stuff["nextPageCursor"], "limit": 100, "sortOrder": "Asc"}
            stuff = await self.request.request(link, parms=payload)
        return _lists

    async def newest_followers(self):
        _lists = await self._stats_follower("Desc")
        if _lists is None:
            return None
        try:
            return _lists
        except IndexError:
            return

    async def oldest_followers(self):
        _lists = await self._stats_follower("Asc")
        if _lists is None:
            return None
        try:
            return _lists
        except IndexError:
            return

    async def follower_count(self):
        _count = await self.request.request(url=f"https://friends.roblox.com/v1/users/{self._Id}/followers/count")
        return _count["count"]


    async def last_online(self):
        data = {"userIds": [self._Id]}
        _online = await self.request.request(url=f'https://presence.roblox.com/v1/presence/users',method='post',data=data)
        return _online['userPresences'][0]['lastOnline']
    async def is_premium(self):
        r = await self.request.html_request(url=f'https://premiumfeatures.roblox.com/v1/users/{self._Id}/validate-membership',method='get',data=None)
        if r == "true":
            r = True
        elif r == 'false':
            r = False
        else:
            r = None
        return r

