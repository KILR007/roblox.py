import aiohttp
import json
import requests.utils as u
import requests
from .ex import NotAuthenticated

def login(cookies):
    #cookies = None
    xcrsftoken = requests.get("https://roblox.com/home").text.split("Roblox.XsrfToken.setToken('")[1].split("');")[0]
    cookies_list = {
        '.ROBLOSECURITY': cookies
    }
    headers = {
        'Origin': 'https://www.roblox.com',
        'X-CSRF-TOKEN': xcrsftoken,
        }
    r = requests.get('https://www.roblox.com/game/GetCurrentUser.ashx', cookies=cookies_list, headers=headers)
    print(r.text)
    if r.text != 'null':
        cookies = cookies
        print(r.text, '33')
        return cookies.get('ROBLOSECURITY')
    else:
        raise NotAuthenticated("Invalid Cookies ")

async def request(url,method,cookies,data=None,parms=None):
    method = method.lower()
    cookies ={'.ROBLOSECURITY': cookies}
    if method == 'post':
        print(cookies)
        async with aiohttp.ClientSession(cookies=cookies)as session:
            async with session.get(url=f'https://roblox.com/home') as smth:
                text = await smth.text()
                xcrsftoken = text.split("Roblox.XsrfToken.setToken('")[1].split("');")[0]
            headers = {
                'Origin': 'https://www.roblox.com',
                'X-CSRF-TOKEN': xcrsftoken,
            }
            async with session.post(url=url, data=json.dumps(data),params=parms,headers=headers) as rep:
                return await rep.text()


    if method == 'delete':
        async with aiohttp.ClientSession(cookies=cookies,trust_env=True) as session:
            async with session.get(url=f'https://roblox.com/home') as smth:
                text = await smth.text()
                xcrsftoken = text.split("Roblox.XsrfToken.setToken('")[1].split("');")[0]
            headers = {
                'Origin': 'https://www.roblox.com',
                'X-CSRF-TOKEN': xcrsftoken,
            }
            async with session.delete(url=url,params=parms,headers=headers) as rep:
                return await rep.json()
    if method == 'patch':
        async with aiohttp.ClientSession(cookies=cookies,trust_env=True) as session:
            async with session.get(url=f'https://roblox.com/home') as smth:
                text = await smth.text()
                xcrsftoken = text.split("Roblox.XsrfToken.setToken('")[1].split("');")[0]
            headers = {
                'Origin': 'https://www.roblox.com',
                'X-CSRF-TOKEN': xcrsftoken,
            }
            async with session.patch(url=url, data=json.dumps(data),params=parms,headers=headers) as rep:
                return await rep.json()
    if method == 'get':
        async with aiohttp.ClientSession(trust_env=True,cookies=cookies) as session:
            async with session.get(url=f'https://roblox.com/home') as smth:
                text = await smth.text()
                xcrsftoken = text.split("Roblox.XsrfToken.setToken('")[1].split("');")[0]
            headers = {
                'Origin': 'https://www.roblox.com',
                'X-CSRF-TOKEN': xcrsftoken,
            }
            async with session.get(url=url,params=parms,headers=headers) as rep:
                return await rep.json()




async def send_request(url,**kwargs):
    parms = None
    #session:aiohttp.ClientSession
    print(f'request for {url}')
    if "parms" in kwargs:
        parms = kwargs['parms']

    async with aiohttp.ClientSession() as session:
        async with session.get(f'{url}', params=parms,
                                headers={"content-type": "application/json"}) as response:

            return await response.json()



