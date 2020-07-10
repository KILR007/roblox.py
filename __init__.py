'''
MIT License

Copyright (c) 2020 KILR007

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
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











