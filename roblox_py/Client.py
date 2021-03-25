from .utils import Requests
from .GroupInfo import GroupInfo
from .Auth_Group import GroupAuth
from .PlayerInfo import PlayerInfo
from .exceptions import GroupNotFound,PlayerNotFound,GameNotFound
from .Auth_Player import PlayerAuth
from .BundleInfo  import BundleInfo
from .AssetInfo import AssetInfo
from .Join_Game import JoinGame
from .GamepassInfo import GamepassInfo
from .BadgeInfo import BadgeInfo
from .PlaceInfo import PlaceInfo
import aiohttp
import json
class Client:

    def __init__(self, cookies=None):
        self.cookies = cookies
        self.request = Requests(cookies=cookies)
        
    async def get_cookies_from_credentials(self, username_or_email, password, type, token):
        type = type.lower()
        dict_e = None
        if type == "email":
            dict_e = {
                "ctype": "Email",
                "cvalue": f"{username_or_email}",
                "password": f"{password}",
            }
        if type == "username":
            dict_e = {
                "ctype": "Username",
                "cvalue": username_or_email,
                "password": password
            }
        async with aiohttp.ClientSession() as ses:
            async with ses.post(url="https://www.roblox.com/favorite/toggle") as smth:
                try:
                    xcrsftoken = smth.headers["X-CSRF-TOKEN"]
                except KeyError:
                    xcrsftoken = ""
            dict_e = json.dumps(dict_e)

            async with ses.post(url=f'https://auth.roblox.com/v2/login', data=dict_e, headers={
                'X-CSRF-TOKEN': xcrsftoken,
                'DNT': '1',
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                'Content-type': 'application/json',
                'Accept': 'application/json',
                'referer': 'www.roblox.com', }) as f:
                josn = await f.json()
            if f.status == 403:
                if josn['errors'][0]['message'] == 'You must pass the robot test before logging in.':
                    et = await token.solve(ckey=f'476068BF-9607-4799-B53D-966BE98E2B81')
                    if type == "email":
                        dict_e = {
                            "ctype": "Email",
                            "cvalue": username_or_email,
                            "password": password,
                            'captchaToken': et,
                            "captchaProvider": 'PROVIDER_ARKOSE_LABS'}
                    if type == 'username':
                        dict_e = {
                            "ctype": "Username",
                            "cvalue": username_or_email,
                            "password": password,
                            'captchaToken': et,
                            "captchaProvider": 'PROVIDER_ARKOSE_LABS'}
                    dict_e = json.dumps(dict_e)
                    async with ses.post(url=f'https://auth.roblox.com/v2/login', data=dict_e) as no:
                        return no.cookies
    async def get_group_info(self, group_id: int):
        idkdd = isinstance(group_id, str)
        if idkdd:
            raise TypeError(f"{group_id} must be an integer")
        yes = GroupInfo(groupID=group_id,request=self.request)
        await yes.update()
        return yes

    async def get_group_by_name(self,group_name:str):
        _eep = await self.request.request(url=f"https://groups.roblox.com/v1/groups/search/lookup?groupName={group_name}",method='get')
        _lis = []
        if _eep['data'] is []:
            raise GroupNotFound
        for data in _eep["data"]:
            idd = data.get("id")
            name = data.get("name")
            e = dict(name=name, id=idd)
            _lis.append(e)
        return _lis
    async def get_user_by_name(self,username:str):
        url = f"https://api.roblox.com/users/get-by-username"
        pars = {'username': username}
        json1 = await self.request.request(url=url, parms=pars,method='get')
        if "Id" not in json1.keys():
            raise PlayerNotFound("Username is Invalid")
        else:
            e = PlayerInfo(playerID=json1['Id'],request=self.request)
            await e.update()
            return e


    async def get_user_info(self,Player_Id:int):
        idkdd = isinstance(Player_Id, str)
        if idkdd:
            raise TypeError(f"{Player_Id} must be an integer")
        yes = PlayerInfo(playerID=Player_Id,request=self.request)
        await yes.update()
        return yes

    async def get_auth_user(self):
        return PlayerAuth(request=self.request)

    async def get_auth_group(self, Group_Id: int):
        idkdd = isinstance(Group_Id, str)
        if idkdd:
            raise TypeError(f"{Group_Id} must be an integer")
        return GroupAuth(groupID=Group_Id,request=self.request)
    async def get_bundle(self,Bundle_ID:int):
        idkdd = isinstance(Bundle_ID, str)
        if idkdd:
            raise TypeError(f"{Bundle_ID} must be an integer")
        yes = BundleInfo(bundleID=Bundle_ID,request=self.request)
        await yes.update()
        return yes


    async def get_asset(self, Asset_id: int):
        idkdd = isinstance(Asset_id, str)
        if idkdd:
            raise TypeError(f"{Asset_id} must be an integer")
        yes = AssetInfo(assetID=Asset_id,request=self.request)
        await yes.update()
        return yes
    async def get_gamepass(self,gamepass_id: int):
        idkdd = isinstance(gamepass_id, str)
        if idkdd:
            raise TypeError(f"{gamepass_id} must be an integer")
        yes = GamepassInfo(gamepassID=gamepass_id,request=self.request)
        await yes.update()
        return yes
    async def join_game(self,PlaceID,roblox_folder_path=None,roblox_game_path=None):
        idkdd = isinstance(PlaceID, str)
        if idkdd:
            raise TypeError(f"{PlaceID} must be an integer")
        return JoinGame(Game_ID=PlaceID,request=self.request,roblox_folder_path=roblox_folder_path,roblox_game_path=roblox_game_path)






    async def get_badge(self,badge_id:int):
        idkdd = isinstance(badge_id, str)
        if idkdd:
            raise TypeError(f"{badge_id} must be an integer")
        e = BadgeInfo(badge_id=badge_id, request=self.request)
        await e.update()
        return e


    async def get_place(self,unverise_id):
        e = PlaceInfo(universe_id=unverise_id, request=self.request)
        await e.update()
        return e

    async def get_place_by_id(self,place_id:int):
        idkdd = isinstance(place_id, str)
        if idkdd:
            raise TypeError(f"{place_id} must be an integer")
        r = await self.request.request(url=f'https://games.roblox.com/v1/games/multiget-place-details?placeIds={place_id}',method='get')

        if r is []:
            raise GameNotFound("Invalid Game ID")
        e = PlaceInfo(universe_id=r[0]['universeId'], request=self.request)
        await e.update()
        return e


