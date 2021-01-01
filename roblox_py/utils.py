from .exceptions import *
import warnings
import json
from .https_session import Http
class Requests:
    def __init__(self,cookies=None):
        self.cookies = cookies
        cookies_list = {'.ROBLOSECURITY': self.cookies}

        self.xcrsftoken = None
        self.headers = {
                    'X-CSRF-TOKEN': self.xcrsftoken,
                    'DNT': '1',
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                    'Content-type': 'application/json',
                    'Accept': 'application/json'
                }
        self.session = Http(cookies=cookies_list)

    async def get_xcrsftoken(self):
        async with self.session as ses:
            async with ses.fetch.post(url=f'https://roblox.com/home') as smth:
                text = await smth.text()
                xcrsftoken = text.split("Roblox.XsrfToken.setToken('")[1].split("');")[0]
                self.xcrsftoken = xcrsftoken
    async def request(self,url, method=None,  data=None, parms=None):
        if method is None:
            method = 'get'
        if self.xcrsftoken is None:
            await self.get_xcrsftoken()
        if data is not None:
            data = json.dumps(data)
        header = {
            'X-CSRF-TOKEN': self.xcrsftoken,
            'DNT': '1',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }
        if method == 'post':
            async with self.session as ses:

                async with ses.fetch.post(url=url, data=data, params=parms,headers=header) as rep:
                    json_text = await rep.json()
                    if rep.status == 403:
                        if json_text['errors'][0]['message'] == 'Token Validation Failed':
                            self.xcrsftoken = None
                            await self.get_xcrsftoken()
                            await self.request(url=url,data=data,method=method,parms=parms)
                        else:
                            try:
                                raise Forbidden(json_text['errors'][0]['message'])
                            except KeyError:
                                raise Forbidden(json_text)

                    if rep.status == 401:
                        try:
                            raise Unauthorized(json_text['errors'][0]['message'])
                        except KeyError:
                            raise Unauthorized(json_text)
                    if rep.status == 429:
                        try:
                            raise RateLimited(json_text['errors'][0]['message'])
                        except KeyError:
                            raise RateLimited(json_text)
                    if rep.status == 503:
                        try:
                            raise ServiceUnavailable(json_text["errors"][0]['message'])
                        except KeyError:
                            raise ServiceUnavailable(json_text)
                    if rep.status == 500:
                        try:
                            raise InternalServiceError(json_text['errors'][0]['message'])
                        except KeyError:
                            raise InternalServiceError(json_text)
                    if rep.status == 400:
                        try:
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
                        except KeyError:
                            warnings.warn(json_text)
                return json_text

        if method == 'delete':
            async with self.session as ses:
                async with ses.fetch.delete(url=url, params=parms,headers=header) as rep:
                    json_text = await rep.json()
                    if rep.status == 403:
                        if json_text['errors'][0]['message'] == 'Token Validation Failed':
                            self.xcrsftoken = None
                            await self.get_xcrsftoken()
                            await self.request(url=url, data=data, method=method, parms=parms)
                        else:
                            try:
                                raise Forbidden(json_text['errors'][0]['message'])
                            except KeyError:
                                raise Forbidden(json_text)

                    if rep.status == 401:
                        try:
                            raise Unauthorized(json_text['errors'][0]['message'])
                        except KeyError:
                            raise Unauthorized(json_text)
                    if rep.status == 429:
                        try:
                            raise RateLimited(json_text['errors'][0]['message'])
                        except KeyError:
                            raise RateLimited(json_text)
                    if rep.status == 503:
                        try:
                            raise ServiceUnavailable(json_text["errors"][0]['message'])
                        except KeyError:
                            raise ServiceUnavailable(json_text)
                    if rep.status == 500:
                        try:
                            raise InternalServiceError(json_text['errors'][0]['message'])
                        except KeyError:
                            raise InternalServiceError(json_text)
                    if rep.status == 400:
                        try:
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
                        except KeyError:
                            warnings.warn(json_text)
                return json_text
        if method == 'patch':
            async with self.session as ses:
                async with ses.fetch.patch(url=url, data=data, params=parms,headers=header) as rep:
                    json_text = await rep.json()

                    if rep.status == 403:
                        if json_text['errors'][0]['message'] == 'Token Validation Failed':
                            self.xcrsftoken = None
                            await self.get_xcrsftoken()
                            await self.request(url=url, data=data, method=method, parms=parms)
                        else:
                            try:
                                raise Forbidden(json_text['errors'][0]['message'])
                            except KeyError:
                                raise Forbidden(json_text)

                    if rep.status == 401:
                        try:
                            raise Unauthorized(json_text['errors'][0]['message'])
                        except KeyError:
                            raise Unauthorized(json_text)
                    if rep.status == 429:
                        try:
                            raise RateLimited(json_text['errors'][0]['message'])
                        except KeyError:
                            raise RateLimited(json_text)
                    if rep.status == 503:
                        try:
                            raise ServiceUnavailable(json_text["errors"][0]['message'])
                        except KeyError:
                            raise ServiceUnavailable(json_text)
                    if rep.status == 500:
                        try:
                            raise InternalServiceError(json_text['errors'][0]['message'])
                        except KeyError:
                            raise InternalServiceError(json_text)
                    if rep.status == 400:
                        try:
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
                        except KeyError:
                            warnings.warn(json_text)
                return json_text
        if method == 'get':
            async with self.session as ses:
                async with ses.fetch.get(url=url, params=parms,headers=header) as rep:
                    json_text = await rep.json()

                    if rep.status == 403:
                        if json_text['errors'][0]['message'] == 'Token Validation Failed':
                            self.xcrsftoken = None
                            await self.get_xcrsftoken()
                            await self.request(url=url, data=data, method=method, parms=parms)
                        else:
                            try:
                                raise Forbidden(json_text['errors'][0]['message'])
                            except KeyError:
                                raise Forbidden(json_text)

                    if rep.status == 401:
                        try:
                            raise Unauthorized(json_text['errors'][0]['message'])
                        except KeyError:
                            raise Unauthorized(json_text)
                    if rep.status == 429:
                        try:
                            raise RateLimited(json_text['errors'][0]['message'])
                        except KeyError:
                            raise RateLimited(json_text)
                    if rep.status == 503:
                        try:
                            raise ServiceUnavailable(json_text["errors"][0]['message'])
                        except KeyError:
                            raise ServiceUnavailable(json_text)
                    if rep.status == 500:
                        try:
                            raise InternalServiceError(json_text['errors'][0]['message'])
                        except KeyError:
                            raise InternalServiceError(json_text)
                    if rep.status == 400:
                        try:
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
                        except KeyError:
                            warnings.warn(json_text)
                return json_text






