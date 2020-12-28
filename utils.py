import aiohttp
import json
import requests
from .exceptions import *
import warnings
async def login(cookies):

    async with aiohttp.ClientSession() as session:
        async with session.get("https://roblox.com/home") as resp:
            text = await resp.text()
            xcrsftoken  = text.split("Roblox.XsrfToken.setToken('")[1].split("');")[0]
    #xcrsftoken = requests.get().text.split("Roblox.XsrfToken.setToken('")[1].split("');")[0]
    cookies_list = {
        '.ROBLOSECURITY': cookies
    }
    headers = {
        'Origin': 'https://www.roblox.com',
        'X-CSRF-TOKEN': xcrsftoken,
    }
    async with aiohttp.ClientSession(cookies=cookies_list) as session:
        async with session.get('https://www.roblox.com/game/GetCurrentUser.ashx',headers=headers) as pes:
            text = await pes.read()
            if text != 'null':
                return dict(is_valid=True,authenticated_userId=text.decode())
            else:
                raise NotAuthenticated("Invalid Cookies")



async def request(url,method,cookies,data=None,parms=None):
    method = method.lower()
    cookies ={'.ROBLOSECURITY': cookies}
    if method == 'post':
        async with aiohttp.ClientSession(cookies=cookies)as session:
            async with session.get(url=f'https://roblox.com/home') as smth:
                text = await smth.text()
                xcrsftoken = text.split("Roblox.XsrfToken.setToken('")[1].split("');")[0]
            headers = {
                'Origin': 'https://www.roblox.com',
                'X-CSRF-TOKEN': xcrsftoken,
                "content-type": "application/json"
            }
            async with session.post(url=url, data=json.dumps(data),params=parms,headers=headers) as rep:
                json_text = await rep.json()
                if rep.status == 403:
                    raise Forbidden(json_text['errors'][0]['message'])
                if rep.status == 429:
                    raise RateLimited(json_text['errors'][0]['message'])
                if rep.status == 503:
                    raise ServiceUnavailable(json_text["errors"][0]['message'])
                if rep.status == 500:
                    raise InternalServiceError(json_text['errors'][0]['message'])
                if rep.status == 400:
                    if json_text['errors'][0]['message'] == 'The target user is invalid or does not exist.':
                        raise PlayerNotFound(json_text['errors'][0]['message'])
                    if json_text['errors'][0]['message'] == 'Group is invalid or does not exist.':
                        raise GroupNotFound(json_text['errors'][0]['message'])
                    if json_text['errors'][0]['message'] == 'Invalid bundle':
                        raise BundleNotFound(json_text['errors'][0]['message'])
                    if json_text['errors'][0]['message'] == 'Invalid assetId':
                        raise AssetNotFound(json_text['errors'][0]['message'])
                    else:
                        warnings.warn(json_text['errors'][0]['message'])
                    return json_text


    if method == 'delete':
        async with aiohttp.ClientSession(cookies=cookies) as session:
            async with session.get(url=f'https://roblox.com/home') as smth:
                text = await smth.text()
                xcrsftoken = text.split("Roblox.XsrfToken.setToken('")[1].split("');")[0]
            headers = {
                'Origin': 'https://www.roblox.com',
                'X-CSRF-TOKEN': xcrsftoken,
                "content-type": "application/json"
            }
            async with session.delete(url=url,params=parms,headers=headers) as rep:
                json_text = await rep.json()
                if rep.status == 403:
                    raise Forbidden(json_text['errors'][0]['message'])
                if rep.status == 429:
                    raise RateLimited(json_text['errors'][0]['message'])
                if rep.status == 503:
                    raise ServiceUnavailable(json_text["errors"][0]['message'])
                if rep.status == 500:
                    raise InternalServiceError(json_text['errors'][0]['message'])
                if rep.status == 400:
                    if json_text['errors'][0]['message'] == 'The target user is invalid or does not exist.':
                        raise PlayerNotFound(json_text['errors'][0]['message'])
                    if json_text['errors'][0]['message'] == 'Group is invalid or does not exist.':
                        raise GroupNotFound(json_text['errors'][0]['message'])
                    if json_text['errors'][0]['message'] == 'Invalid bundle':
                        raise BundleNotFound(json_text['errors'][0]['message'])
                    if json_text['errors'][0]['message'] == 'Invalid assetId':
                        raise AssetNotFound(json_text['errors'][0]['message'])
                    else:
                        warnings.warn(json_text['errors'][0]['message'])
                return json_text
    if method == 'patch':
        async with aiohttp.ClientSession(cookies=cookies,trust_env=True) as session:
            async with session.get(url=f'https://roblox.com/home') as smth:
                text = await smth.text()
                xcrsftoken = text.split("Roblox.XsrfToken.setToken('")[1].split("');")[0]
            headers = {
                'Origin': 'https://www.roblox.com',
                'X-CSRF-TOKEN': xcrsftoken,
                "content-type": "application/json"
            }
            async with session.patch(url=url, data=json.dumps(data),params=parms,headers=headers) as rep:
                json_text = await rep.json()
                if rep.status == 403:
                    raise Forbidden(json_text['errors'][0]['message'])
                if rep.status == 429:
                    raise RateLimited(json_text['errors'][0]['message'])
                if rep.status == 503:
                    raise ServiceUnavailable(json_text["errors"][0]['message'])
                if rep.status == 500:
                    raise InternalServiceError(json_text['errors'][0]['message'])
                if rep.status == 400:
                    if json_text['errors'][0]['message'] == 'The target user is invalid or does not exist.':
                        raise PlayerNotFound(json_text['errors'][0]['message'])
                    if json_text['errors'][0]['message'] == 'Group is invalid or does not exist.':
                        raise GroupNotFound(json_text['errors'][0]['message'])
                    if json_text['errors'][0]['message'] == 'Invalid bundle':
                        raise BundleNotFound(json_text['errors'][0]['message'])
                    if json_text['errors'][0]['message'] == 'Invalid assetId':
                        raise AssetNotFound(json_text['errors'][0]['message'])
                    else:
                        warnings.warn(json_text['errors'][0]['message'])
                return json_text
    if method == 'get':
        async with aiohttp.ClientSession(trust_env=True,cookies=cookies) as session:
            async with session.get(url=f'https://roblox.com/home') as smth:
                text = await smth.text()
                xcrsftoken = text.split("Roblox.XsrfToken.setToken('")[1].split("');")[0]
            headers = {
                'Origin': 'https://www.roblox.com',
                'X-CSRF-TOKEN': xcrsftoken,
                "content-type": "application/json"
            }
            async with session.get(url=url,params=parms,headers=headers) as rep:
                json_text = await rep.json()
                if rep.status == 403:
                    raise Forbidden(json_text['errors'][0]['message'])
                if rep.status == 429:
                    raise RateLimited(json_text['errors'][0]['message'])
                if rep.status == 503:
                    raise ServiceUnavailable(json_text["errors"][0]['message'])
                if rep.status == 500:
                    raise InternalServiceError(json_text['errors'][0]['message'])
                if rep.status == 400:
                    if json_text['errors'][0]['message'] == 'The target user is invalid or does not exist.':
                        raise PlayerNotFound(json_text['errors'][0]['message'])
                    if json_text['errors'][0]['message'] == 'Group is invalid or does not exist.':
                        raise GroupNotFound(json_text['errors'][0]['message'])
                    if json_text['errors'][0]['message'] == 'Invalid bundle':
                        raise BundleNotFound(json_text['errors'][0]['message'])
                    if json_text['errors'][0]['message'] == 'Invalid assetId':
                        raise AssetNotFound(json_text['errors'][0]['message'])
                    else:
                        warnings.warn(json_text['errors'][0]['message'])

                return json_text




async def send_request(url,**kwargs):
    parms = None
    if "parms" in kwargs:
        parms = kwargs['parms']

    async with aiohttp.ClientSession() as session:
        async with session.get(f'{url}', params=parms, headers={"content-type": "application/json"}) as rep:
            json_text = await rep.json()
            if rep.status == 403:
                raise Forbidden(json_text['errors'][0]['message'])
            if rep.status == 429:
                raise RateLimited(json_text['errors'][0]['message'])
            if rep.status == 503:
                raise ServiceUnavailable(json_text["errors"][0]['message'])
            if rep.status == 500:
                raise InternalServiceError(json_text['errors'][0]['message'])
            if rep.status == 400:
                if json_text['errors'][0]['message'] == 'The target user is invalid or does not exist.':
                    raise PlayerNotFound(json_text['errors'][0]['message'])
                if json_text['errors'][0]['message'] == 'Group is invalid or does not exist.':
                    raise GroupNotFound(json_text['errors'][0]['message'])
                if json_text['errors'][0]['message'] == 'Invalid bundle':
                    raise BundleNotFound(json_text['errors'][0]['message'])
                if json_text['errors'][0]['message'] == 'Invalid assetId':
                    raise AssetNotFound(json_text['errors'][0]['message'])
                else:
                    raise UnknownError(json_text['errors'][0]['message'])
            return json_text



