

import requests
group_id1 = None
class Groupnotfound(Exception):
    """ Raised When Group Is Not Found"""
class Badarguement(Exception):
    """Raised When Site Returns Status Code Other Than 200"""
def sendreq(url):
    pp = requests.get(url)
    if pp.status_code == 200:
        return pp.json()
    else:
        raise Badarguement
class Groups:
    def __init__(self,group_id:int):
        global group_id1
        group_id1 = group_id
        url = f"https://api.roblox.com/groups/{group_id1}"

        noobs = requests.get(url)
        if noobs.status_code == 200:
            noobss = noobs.json()
            if "Name" not in noobss.keys():
                raise Groupnotfound


        else:
            raise Badarguement
    def group_enemies(self):
        lala = requests.get(f"https://api.roblox.com/groups/{group_id1}/enemies").json()
        if lala["Groups"] == []:
            return None
        xddddd = []
        for good in lala['Groups']:
            name = good.get("Name")
            xddddd.append(name)
        return xddddd


    @staticmethod
    def group_allies():
        lala = requests.get(f"https://api.roblox.com/groups/{group_id1}/allies").json()
        if lala["Groups"] == []:
            return None
        xddddd = []
        for good in lala['Groups']:
            name = good.get("Name")
            xddddd.append(name)
        return xddddd
    @staticmethod
    def group_name():
        DC = sendreq(f"https://groups.roblox.com/v1/groups/{group_id1}")
        return DC["name"]
    @staticmethod
    def group_id():
        DC = sendreq(f"https://groups.roblox.com/v1/groups/{group_id1}")
        return DC["id"]
    @staticmethod
    def group_owner_name():
        DC = sendreq(f"https://groups.roblox.com/v1/groups/{group_id1}")
        return DC["owner"]["username"]
    @staticmethod
    def group_owner_id():
        DC = sendreq(f"https://groups.roblox.com/v1/groups/{group_id1}")
        return DC["owner"]["userId"]
    @staticmethod
    def group_member_count():
        DC = sendreq(f"https://groups.roblox.com/v1/groups/{group_id1}")
        return DC["memberCount"]

    @staticmethod
    def is_private():
        DC = sendreq(f"https://groups.roblox.com/v1/groups/{group_id1}")
        if DC["publicEntryAllowed"] == True:
            return False
        else:
            return True

    @staticmethod
    def group_shout():
        DC = sendreq(f"https://groups.roblox.com/v1/groups/{group_id1}")
        if DC["shout"]["body"] == "":
            return None
        else:
            return DC["shout"]["body"]

    @staticmethod
    def group_shout_poster_name():
        DC = sendreq(f"https://groups.roblox.com/v1/groups/{group_id1}")
        if DC["shout"]["body"] == "":
            return None
        else:
            return DC["shout"]["poster"]["username"]
    @staticmethod
    def group_thumbnail():
        DC = sendreq(f"https://www.roblox.com/group-thumbnails?params=%5B%7BgroupId:{group_id1}%7D%5D")
        return DC[0]["thumbnailUrl"]
    @staticmethod
    def group_url():
        DC = sendreq(f"https://www.roblox.com/group-thumbnails?params=%5B%7BgroupId:{group_id1}%7D%5D")
        return DC[0]["url"]
    @staticmethod
    def group_description():
        DC = sendreq(f"https://groups.roblox.com/v1/groups/{group_id1}")
        if DC["description"] == "":
            return None
        else:
            return DC["description"]


















