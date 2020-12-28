from .utils import send_request,login
from .Groups import GroupInfo
from .Auth_Group import GroupAuth
from .Player import PlayerInfo
from .exceptions import GroupNotFound,PlayerNotFound,BundleNotFound,AssetNotFound
from .Auth_Player import PlayerAuth
from .Bundle  import BundleInfo
from .Asset import AssetInfo
class Client:

    def __init__(self, cookies=None, proxies=None):
        self.cookies = cookies
        self.proxies = proxies
    async def is_valid(self):
        if self.cookies is not None:
            e = await login(cookies=self.cookies)
            return e

    async def get_group_info(self, group_id: int):
        idkdd = isinstance(group_id, str)
        if idkdd:
            raise TypeError(f"{group_id} must be an integer")
        eee = await send_request(f"https://groups.roblox.com/v1/groups/{group_id}")
        return GroupInfo(groupID=group_id,smth=eee)

    async def get_group_by_name(self,group_name:str):
        _eep = await send_request(f"https://groups.roblox.com/v1/groups/search/lookup?groupName={group_name}")
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
        json1 = await send_request(url=url, parms=pars)
        if "Id" not in json1.keys():
            raise PlayerNotFound("Username is Invalid")
        else:
            return json1['Id']
    async def get_user_info(self,Player_Id:int):
        idkdd = isinstance(Player_Id, str)
        if idkdd:
            raise TypeError(f"{Player_Id} must be an integer")
        xd = await send_request(url=f"https://users.roblox.com/v1/users/{Player_Id}")
        return PlayerInfo(playerID=xd['Id'],alr=xd)

    async def get_auth_user(self):
        return PlayerAuth(cookies=self.cookies)

    async def get_auth_group(self, Group_Id: int):
        idkdd = isinstance(Group_Id, str)
        if idkdd:
            raise TypeError(f"{Group_Id} must be an integer")
        return GroupAuth(groupID=Group_Id, cookies=self.cookies)
    async def get_bundle(self,Bundle_ID:int):
        idkdd = isinstance(Bundle_ID, str)
        if idkdd:
            raise TypeError(f"{Bundle_ID} must be an integer")
        Noob = await send_request(url=f"https://catalog.roblox.com/v1/bundles/{Bundle_ID}/details")
        return BundleInfo(bundleID=Bundle_ID, json_obj=Noob)


    async def get_asset(self, Asset_id: int):
        r = await send_request(url=f"http://api.roblox.com/Marketplace/ProductInfo?assetId={Asset_id}")
        idkdd = isinstance(Asset_id, str)
        if idkdd:
            raise TypeError(f"{Asset_id} must be an integer")
        return AssetInfo(assetID=Asset_id, json_obj=r)







