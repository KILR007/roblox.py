

import requests
dat = None
smth = None
class Playernotfound(Exception):
    """ Raised When Player Is Not Found"""
class Badarguement(Exception):
    """Raised When Site Returns Status Code Other Than 200"""
def sendreq(url):
    pp = requests.get(url)
    if pp.status_code == 200:
        return pp.json()
    else:
        raise Badarguement

class Players:
    def __init__(self,username1):
        self.username = username1
        url = f"https://api.roblox.com/users/get-by-username?username={username1}"
        f = requests.get(url)
        if f.status_code == 200:
            pass
        else:
            er = Badarguement(f"Site Has Return {f.status_code} Code")
            raise er
        global dat
        dat = f.json()
        if "Id" not in dat:
            Error = Playernotfound("Player Not Found!")
            raise Error
        else:
            dat = dat["Id"]

    @staticmethod
    def user_id():
        e = dat
        return e

    @staticmethod
    def description():
        e = dat
        url = f"https://users.roblox.com/v1/users/{e}"
        nothin = requests.get(url)
        if nothin.status_code == 200:
            nothing = nothin.json()
            desc = nothing["description"]
            if desc == "":
                return None
            else:
                return desc
        else:
            er = Badarguement(f"Site Has Return {nothin.status_code} Code")
            raise er

    @staticmethod
    def created_at():
        e = dat
        url = f"https://users.roblox.com/v1/users/{e}"
        ee = requests.get(url)
        if ee.status_code == 200:
            nothingd = ee.json()
            c = nothingd["created"]
            if c == "":
                return None
            else:
                return c
        else:
            er = Badarguement(f"Site Has Return {ee.status_code} Code")
            raise er

    @staticmethod
    def roblox_badges():
        f = dat
        url = f"https://www.roblox.com/badges/roblox?userId={f}"
        mm2 = requests.get(url)
        if mm2.status_code == 200:
            mm = mm2.json()
            if "RobloxBadges" not in mm:
                return None
            else:
                string = []
                for item in mm["RobloxBadges"]:
                    string.append(f'{item["Name"]}')
                if string == []:
                    return None
                return string
        else:
            er = Badarguement(f"Site Has Return {mm2.status_code} Code")
            raise er

    @staticmethod
    def url():
        f = dat
        return f"https://www.roblox.com/users/{f}/profile"

    @staticmethod
    def friends():
        f = dat
        lr = f"https://friends.roblox.com/v1/users/{f}/friends"
        pp = requests.get(lr)
        if pp.status_code == 200:
            p = pp.json()
            lists = []
            for bill in p['data']:
                pp = bill.get('name')
                lists.append(pp)
            return lists
        else:
            er = Badarguement(f"Site Has Return {pp.status_code} Code")
            raise er

    @staticmethod
    def latest_friend():
        try:
            f = dat
            lr = f"https://friends.roblox.com/v1/users/{f}/friends"
            pp = requests.get(lr)
            if pp.status_code == 200:
                p = pp.json()
                return p["data"][0]["name"]
            else:
                er = Badarguement(f"Site Has Return {pp.status_code} Code")
                raise er
        except IndexError:
            return None

    @staticmethod
    def friends_count():
        f = dat
        lr = f"https://friends.roblox.com/v1/users/{f}/friends"
        pp = requests.get(lr)
        if pp.status_code == 200:
            p = pp.json()
            return len(p["data"])
        else:
            er = Badarguement(f"Site Has Return {pp.status_code} Code")
            raise er

    @staticmethod
    def oldest_friend():
        f = dat
        lr = f"https://friends.roblox.com/v1/users/{f}/friends"
        pp = requests.get(lr)
        if pp.status_code == 200:
            p = pp.json()
            if len(p["data"]) == 0:
                return None
            else:
                D = len(p["data"]) - 1
                return p["data"][D]["name"]
        else:
            er = Badarguement(f"Site Has Return {pp.status_code} Code")
            raise er

    @staticmethod
    def groups():
        f = dat
        ulr = f"https://api.roblox.com/users/{f}/groups"
        p = requests.get(ulr)
        if p.status_code == 200:
            pp = p.json()
            lists = []
            for bill in pp:
                pp = bill.get('Name')
                lists.append(pp)
            return lists
        else:
            er = Badarguement(f"Site Has Return {p.status_code} Code")
            raise er

    @staticmethod
    def latest_group():
        f = dat
        ulr = f"https://api.roblox.com/users/{f}/groups"
        p = requests.get(ulr)
        if p.status_code == 200:
            try:
                pp = p.json()
                return pp[0]["Name"]
            except IndexError:
                return None

        else:
            er = Badarguement(f"Site Has Return {p.status_code} Code")
            raise er

    @staticmethod
    def oldest_group():
        f = dat
        ulr = f"https://api.roblox.com/users/{f}/groups"
        p = requests.get(ulr)
        if p.status_code == 200:
            pp = p.json()
            if len(pp) == 0:
                return None
            else:
                D = len(pp) - 1
                return pp[D]["Name"]

        else:
            er = Badarguement(f"Site Has Return {p.status_code} Code")
            raise er

    @staticmethod
    def groups_count():
        f = dat
        ulr = f"https://api.roblox.com/users/{f}/groups"
        p = requests.get(ulr)
        if p.status_code == 200:
            pp = p.json()
            if len(pp) == 0:
                return 0
            else:
                return len(pp)

        else:
            er = Badarguement(f"Site Has Return {p.status_code} Code")
            raise er

    @staticmethod
    def thumbnail():
        f = dat
        ulr = f"https://www.roblox.com/headshot-thumbnail/json?userId={f}&width=180&height=180"
        p = requests.get(ulr)
        if p.status_code == 200:
            pp = p.json()
            return pp["Url"]
        else:
            er = Badarguement(f"Site Has Return {p.status_code} Code")
            raise er

    @staticmethod
    def avatar():
        f = dat
        ulr = f"https://www.roblox.com/headshot-thumbnail/json?userId={f}&width=420&height=420"
        p = requests.get(ulr)
        if p.status_code == 200:
            pp = p.json()
            return pp["Url"]
        else:
            er = Badarguement(f"Site Has Return {p.status_code} Code")
            raise er
