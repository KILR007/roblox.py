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



e(Cookie='_28A7D0A4A36D22BA5B688E0952708C221999C2BA1DD1F0826174554B972DBC75B276BEBAB86FE85D4BA094F26C7CE74B31FD86375DDEFC4448CCD9ABD9F71E152D23053FE3B4D203A62028B5321D5A8A0B0067A8AC9945CE36A3813CAD27B68B44E3A7EFD4732DAA2F1EA56036630F0FF6442192DB2A22ED5BBF19E32FE003F451B21935CEB4CD809B7819A84D3968EBCB01E958D51C66680B2FCF0DE5191547BC659478E858AFE6688A83848CED437259A1588EBD091097096A0B18685A9021EEC0F50D46ED78F7086F670CE6C854A75685436263B37400BE8195E6E068A1A41BD3ECDC92B96287F0EF4B630D1CA5C04ECAE625675DF1CDB884D06D1F1A15C34F510DBCF450C295BF77B66E5A5C1E1DF4339D70CEC23DB03FECE2E346B4787BAFD6B3D1')