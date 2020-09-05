from .utils import sendreq,direct
from .exceptions import GroupNotFound
class Group:
    def __init__(self,ID:int):
        self.ID = ID
        xd = direct(f"https://api.roblox.com/groups/{ID}")
        if "Name" not in xd.keys():
            raise GroupNotFound
        else:
            self.groupss = sendreq(f"https://groups.roblox.com/v1/groups/{ID}")
            self.enimes = sendreq(f"https://api.roblox.com/groups/{ID}/enemies")
            self.alies  = sendreq(f"https://api.roblox.com/groups/{ID}/allies")
class Groups(Group):
    def group_allies(self):
        lala = self.alies
        if lala["Groups"] == []:
            return None
        else:
            xddddd = []
            for good in lala['Groups']:
                name = good.get("Name")
                xddddd.append(name)
            return xddddd

    def group_enemies(self):
        lala = self.enimes
        if lala["Groups"] == []:
            return None
        else:
            xddddd = []
            for good in lala['Groups']:
                name = good.get("Name")
                xddddd.append(name)
            return xddddd

    def group_name(self):
        return self.groupss["name"]
    def group_id(self):
        return self.groupss["id"]
    def group_owner_name(self):
        try:
            return self.groupss["owner"]["username"]
        except TypeError:
            return None
    def group_owner_id(self):
        try:
            return self.groupss["owner"]["userId"]
        except TypeError:
            return None
    def group_member_count(self):
        return self.groupss["memberCount"]
    def is_private(self):
        if self.groupss["publicEntryAllowed"] == True:
            return False
        else:
            return True


    def group_shout(self):
        try:
            if self.groupss["shout"]["body"] == "":
                return None
            else:
                return self.groupss["shout"]["body"]
        except TypeError:
            return None


    def group_shout_poster_name(self):
        try:
            if self.groupss["shout"]["body"] == "":
                return None
            else:
                return self.groupss["shout"]["poster"]["username"]
        except TypeError:
            return None


    def group_thumbnail(self):
        DC = sendreq(f"https://www.roblox.com/group-thumbnails?params=%5B%7BgroupId:{self.ID}%7D%5D")
        return DC[0]["thumbnailUrl"]


    def group_url(self):
        DC = sendreq(f"https://www.roblox.com/group-thumbnails?params=%5B%7BgroupId:{self.ID}%7D%5D")
        return DC[0]["url"]


    def group_description(self):
        try:
            if self.groupss["description"] == "":
                return None
            else:
                return self.groupss["description"]
        except TypeError:
            return None


