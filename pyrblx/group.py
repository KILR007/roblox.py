import requests
class Badarguement(Exception):
    """Raised When Site Returns Status Code Other Than 200"""
class Groupnotfound(Exception):
    """ Raised When Group Is Not Found"""
def sendreq(url):
    pp = requests.get(url)
    if pp.status_code == 200:
        return pp.json()
    else:
        raise Badarguement

DC = None
group_id1 = None
class Groups:
    def __init__(self,group_id:int):
        global group_id1
        group_id1 = group_id
        url = f"https://api.roblox.com/groups/{group_id1}"
        noobs = requests.get(url)
        e = noobs.json()
        if "Name" not in e.keys():
            raise Groupnotfound
        else:
            global DC
            DC = sendreq(f"https://groups.roblox.com/v1/groups/{group_id1}")


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
        return DC["name"]
    @staticmethod
    def group_id():

        return DC["id"]
    @staticmethod
    def group_owner_name():
        try:
            return DC["owner"]["username"]
        except TypeError:
            return None
    @staticmethod
    def group_owner_id():
        try:
            return DC["owner"]["userId"]
        except TypeError:
            return None
    @staticmethod
    def group_member_count():
        return DC["memberCount"]

    @staticmethod
    def is_private():
        if DC["publicEntryAllowed"] == True:
            return False
        else:
            return True

    @staticmethod
    def group_shout():
        try:
            if DC["shout"]["body"] == "":
                return None
            else:
                return DC["shout"]["body"]
        except TypeError:
            return None
    @staticmethod
    def group_shout_poster_name():
        try:
            if DC["shout"]["body"] == "":
                return None
            else:
                return DC["shout"]["poster"]["username"]
        except TypeError:
            return None

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
        try:
            if DC["description"] == "":
                return None
            else:
                return DC["description"]
        except TypeError:
            return None


