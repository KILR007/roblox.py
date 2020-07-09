import requests
dat = None
smth = None

class Players:
    def __init__(self,username):
        self.username = username
        url = f"https://api.roblox.com/users/get-by-username?username={username}"
        f = requests.get(url)
        global dat
        dat = f.json()
    def id(self):
        global dat
        if "Id" not in dat:
            return "User Not Found"
        else:
            e = dat["Id"]
            return e
    def descrition(self):
        global dat
        if "Id" not in dat:
            return "User Not Found"
        else:
            e = dat["Id"]
            url = f"https://users.roblox.com/v1/users/{e}"
            nothing = requests.get(url).json()
            desc = nothing["description"]
            if desc == "":
                return "*No Description*"
            else:
                return desc
    def avatar(self):
        global dat
        if "Id" not in dat:
            return "User Not Found"
        else:
            e = dat["Id"]
            return f"https://www.roblox.com/bust-thumbnail/image?userId={e}&width=100&height=100&format=png"
    def created(self):
        global dat
        if "Id" not in dat:
            return "User Not Found"
        else:
            e = dat["Id"]
            url = f"https://users.roblox.com/v1/users/{e}"
            nothingd = requests.get(url).json()
            c = nothingd["created"]
            if c == "":
                return None
            else:
                return c
    def badges(self):
        global dat
        if "Id" not in dat:
            return "User Not Found"
        else:
            f = dat["Id"]
            url = f"https://www.roblox.com/badges/roblox?userId={f}"
            mm = requests.get(url).json()
            if "RobloxBadges" not in mm:
                return "*No Roblox Badges*"
            else:
                string = ""
                for item in mm["RobloxBadges"]:
                    string += f'{item["Name"]} ,'
                if string == "":
                    return "*No Roblox Badges*"
                return string
    def url(self):
        global dat
        if "Id" not in dat:
            return "User Not Found"
        else:
            f = dat["Id"]
            return f"https://www.roblox.com/users/{f}/profile"











