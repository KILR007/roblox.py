from .utils import Requests
from .Groups import GroupInfo
from .Auth_Group import GroupAuth
from .Player import PlayerInfo
from .exceptions import GroupNotFound,PlayerNotFound
from .Auth_Player import PlayerAuth
from .Bundle  import BundleInfo
from .Asset import AssetInfo
from .Gamepass import GamepassInfo
class Client:

    def __init__(self, cookies=None):
        self.cookies = cookies
        self.request = Requests(cookies=cookies)

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
            return json1['Id']
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
        return GroupAuth(groupID=Group_Id, cookies=self.cookies,request=self.request)
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





