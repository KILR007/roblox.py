from .utis import send_request,login
from .Groups import GroupInfo
from .Player import PlayerInfo
from .ex import GroupNotFound,PlayerNotFound,BundleNotFound,AssetNotFound
from .Auth_Player import PlayerAuth
from .Bundle  import BundleInfo
from .Asset import AssetInfo
class Client:
    """
    Client
    """
    def __init__(self, cookies=None, proxies=None):
        self.cookies = cookies
        self.proxies = proxies
        if cookies is not None:
            login(cookies=cookies)
            print('s')

    async def get_group_by_info(self, group_id: int):
        idkdd = isinstance(group_id, str)
        if idkdd:
            raise TypeError
        eee = await send_request(f"https://groups.roblox.com/v1/groups/{group_id}")
        if "name" not in eee.keys():
            raise GroupNotFound
        else:
            return GroupInfo(group_id,eee)

    async def get_group_by_name(self,group_name:str):
        _eep = await send_request(f"https://groups.roblox.com/v1/groups/search/lookup?groupName={group_name}")
        print(_eep)
        _lis = []
        for data in _eep["data"]:
            idd = data.get("id")
            name = data.get("name")
            e = dict(name=name, id=idd)
            _lis.append(e)
        return _lis
    async def get_player_by_name(self,username:str):
        url = f"https://api.roblox.com/users/get-by-username"
        pars = {'username': username}
        json1 = await send_request(url=url, parms=pars)
        if "Id" not in json1.keys():
            raise PlayerNotFound
        else:
            return json1['Id']
    async def get_player_info(self,Player_Id:int):
        idkdd = isinstance(Player_Id, str)
        if idkdd:
            raise TypeError
        xd = await send_request(url=f"https://users.roblox.com/v1/users/{Player_Id}")
        if "id" not in xd.keys():
            raise PlayerNotFound
        else:
            ea = await send_request(url=f"https://users.roblox.com/v1/users/{Player_Id}")

            return PlayerInfo(xd['Id'],ea)

    async def get_auth_user(self,Player_Id:int):
        idkdd = isinstance(Player_Id, str)
        if idkdd:
            raise TypeError
        xd = await send_request(url=f"https://api.roblox.com/users/{Player_Id}")
        if "Id" not in xd.keys():
            raise PlayerNotFound
        return PlayerAuth(targetId=Player_Id,cookies=None)

    async def get_auth_group(self, Group_Id: int):
        idkdd = isinstance(Group_Id, str)
        if idkdd:
            raise TypeError
        xd = await send_request(url=f"https://api.roblox.com/users/{Group_Id}")
        if "Id" not in xd.keys():
            raise PlayerNotFound
        return PlayerAuth(targetId=Group_Id, cookies=None)
    async def get_bundle(self,Bundle_ID:int):
        idkdd = isinstance(Bundle_ID, str)
        if idkdd:
            raise TypeError

        Noob = await send_request(url=f"https://catalog.roblox.com/v1/bundles/{Bundle_ID}/details")
        if "id" not in Noob.keys():
            raise BundleNotFound
        else:
            return BundleInfo(bundleID=Bundle_ID,json=Noob)

    async def get_asset(self, Asset_id: int):
        r = await send_request(url=f"http://api.roblox.com/Marketplace/ProductInfo?assetId={Asset_id}")
        if "AssetId" not in r.keys():
            raise AssetNotFound
        else:
            return AssetInfo(assetID=Asset_id,json=r)






