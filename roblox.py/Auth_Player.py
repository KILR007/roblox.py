

from .utils import request
from .exceptions import NotAuthenticated
import aiohttp
class PlayerAuth:
    def __init__(self,cookies=None):
        self.cookies = cookies
        if cookies is None:
            raise NotAuthenticated("No Cookies Found")
    async def get_self(self):
        async with aiohttp.ClientSession as ses:
            async with ses.get(f'https://www.roblox.com/game/GetCurrentUser.ashx') as res:
                text = await res.read()
                if text is None:
                    return None
                else:
                    return text.decode()

    async def follow(self,TargetId:int):
        data = {
            'targetUserId': TargetId
        }
        e = await request(url=f'https://friends.roblox.com/v1/users/{TargetId}/follow',method='post',cookies=self.cookies,data=data)
        return e


    async def unfollow(self,TargetId:int):
        data = {
            'targetUserId': TargetId
        }
        e = await request(url=f'https://friends.roblox.com/v1/users/{TargetId}/unfollow',method='post',cookies=self.cookies,data=data)
        return e
    async def block(self,TargetId:int):
        e = await request(url=f'https://accountsettings.roblox.com/v1/users/{TargetId}/block',method='post',cookies=self.cookies)
        return e
    async def unblock(self,TargetId:int):
        e = await request(url=f'https://accountsettings.roblox.com/v1/users/{TargetId}/unblock', method='post',
                          cookies=self.cookies)
        return e

    async def send_friend_request(self,TargetId:int):
        data = {
            'targetUserId': TargetId
        }
        e = await request(url=f'https://friends.roblox.com/v1/users/{TargetId}/request-friendship', method='post',
                          cookies=self.cookies, data=data)
        return e

    async def unfriend(self,TargetId:int):
        data = {
            'targetUserId': TargetId
        }
        e = await request(url=f'https://friends.roblox.com/v1/users/{TargetId}/unfriend', method='post',
                          cookies=self.cookies, data=data)
        return e

    async def friend_request_count(self):

        e = await request(url=f'https://friends.roblox.com/v1/user/friend-requests/count', method='get',
                          cookies=self.cookies)
        return e['count']

    async def decline_request(self,TargetId:int):
        data = {
            'targetUserId': TargetId
        }
        e = await request(url=f'https://friends.roblox.com/v1/users/{TargetId}/decline-friend-request', method='post',
                          cookies=self.cookies, data=data)
        return e

    async def accept_request(self,TargetId:int):
        data = {
            'targetUserId': TargetId
        }
        e = await request(url=f'https://friends.roblox.com/v1/users/{TargetId}/accept-friend-request', method='post',
                          cookies=self.cookies, data=data)
        return e

    async def is_following(self,TargetId:int):
        data = {"targetUserIds": [TargetId]}
        e = await request(url=f'https://friends.roblox.com/v1/user/following-exists',
                          method='post',
                          cookies=self.cookies, data=data)
        return e['followings'][0]['isFollowing']

    async def birth_date(self):
        e = await request(url=f'https://accountinformation.roblox.com/v1/birthdate',cookies=self.cookies,method='get')
        return dict(day=e['birthDay'],month=e['birthMonth'],year=e['birthYear'])
    async def change_birth_day(self,day,month,year):
        data = {
        "birthMonth": month,
        "birthDay": day,
        "birthYear": year}
        e = await request(url=f'https://accountinformation.roblox.com/v1/birthdate',method='post',cookies=self.cookies,data=data)
        return e
    async def gender(self):
        e = await request(url='https://accountinformation.roblox.com/v1/gender',cookies=self.cookies,method='get')
        val =  e['gender']
        gender = None
        if val == 2:
            gender = "Male"
        else:
            gender = "Female"
        return gender
    async def change_gender(self,gender):
        data = dict(gender=gender)

        e = await request(url='https://accountinformation.roblox.com/v1/gender',cookies=self.cookies,method='post',data=data)
        return e
    async def phone(self):
        e = await request(url='https://accountinformation.roblox.com/v1/phone',cookies=self.cookies,method='get')
        return e
    async def set_phone(self,code,prefix,phone,password):
        data = {
        "countryCode": code,
        "prefix": prefix,
        "phone": phone,
        "password": password
        }
        e = await request(url='https://accountinformation.roblox.com/v1/phone',cookies=self.cookies,method='post',data=data)
        return e
    async def metadata(self):
        e = await request(url=f'https://accountinformation.roblox.com/v1/metadata',cookies=self.cookies,method='get')
        return e
    async def delete_phone(self,code,prefix,phone,password):
        data = {
        "countryCode": code,
        "prefix": prefix,
        "phone": phone,
        "password": password
        }
        e = await request(url='https://accountinformation.roblox.com/v1/phone/delete',cookies=self.cookies,method='post',data=data)
        return e
    async def verify_phone(self,code):
        data = dict(code=code)
        e = await request(url='https://accountinformation.roblox.com/v1/phone/verify',method='post',data=data,cookies=self.cookies)
        return e
    async def promotion_channel(self):
        e = await request(url='https://accountinformation.roblox.com/v1/promotion-channels', cookies=self.cookies, method='get')
        return e
    async def set_promotion_channel(self,**kwargs):
        facebook = kwargs.get('facebook',None)
        twitter = kwargs.get('twitter',None)
        youtube = kwargs.get('youtube',None)
        twitch = kwargs.get('twitch',None)
        privacy = kwargs.get('privacy',None)
        data = {
            "facebook": facebook,
            "twitter": twitter,
            "youtube": youtube,
            "twitch": twitch,
            "promotionChannelsVisibilityPrivacy": privacy
        }

        e = await request(url='https://accountinformation.roblox.com/v1/phone/promotion-channels', method='post',
                          data=data,
                          cookies=self.cookies)
        return e
    async def star_code(self):
        e = await request(url=f'https://accountinformation.roblox.com/v1/star-code-affiliates',method='get',cookies=self.cookies)
        return e
    async def change_star_code(self,code):
        data = {"code": code}
        e = await request(url=f'https://accountinformation.roblox.com/v1/star-code-affiliates',method='post',cookies=self.cookies,data=data)
        return e

    async def delete_star_code(self):

        e = await request(url=f'https://accountinformation.roblox.com/v1/star-code-affiliates', method='delete',
                          cookies=self.cookies)
        return e
    async def get_chat_app_privacy(self):
        e = await request(url=f'https://accountsettings.roblox.com/v1/app-chat-privacy',method='get',cookies=self.cookies)
        return e['appChatPrivacy']

    async def change_chat_app_privacy(self,privacy):
        data = {
            "appChatPrivacy": privacy
        }
        e = await request(url=f'https://accountsettings.roblox.com/v1/app-chat-privacy',method='post',cookies=self.cookies,data=data)
        return e
    async def get_game_app_privacy(self):
        e = await request(url=f'https://accountsettings.roblox.com/v1/game-chat-privacy',method='get',cookies=self.cookies)
        return e['gameChatPrivacy']

    async def change_game_app_privacy(self,privacy):
        data = {
            "gameChatPrivacy": privacy
        }
        e = await request(url=f'https://accountsettings.roblox.com/v1/game-chat-privacy',method='post',cookies=self.cookies,data=data)
        return e

    async def get_inventory_privacy(self):
        e = await request(url=f'https://accountsettings.roblox.com/v1/inventory-privacy', method='get',
                          cookies=self.cookies)
        return e['inventoryPrivacy']

    async def change_inventory_privacy(self, privacy):
        data = {
            "inventoryPrivacy": privacy
        }
        e = await request(url=f'https://accountsettings.roblox.com/v1/inventory-privacy', method='post',
                          cookies=self.cookies, data=data)
        return e
    async def get_private_message_privacy(self):
        e = await request(url=f"https://accountsettings.roblox.com/v1/private-message-privacy",method='get',cookies=self.cookies)
        return e['privateMessagePrivacy']
    async def change_private_message_privacy(self,privacy):
        data = {"privateMessagePrivacy": privacy}
        e = await request(url=f"https://accountsettings.roblox.com/v1/private-message-privacy",method='post',data=data,cookies=self.cookies)
    async def get_email(self):
        e  = await request(url='https://accountsettings.roblox.com/v1/email',cookies=self.cookies,method='get')
        return e
    async def change_email(self,new_email,password):
        data = {"password": password,"emailAddress": new_email}
        e = await request(url='https://accountsettings.roblox.com/v1/email',cookies=self.cookies,method='post',data=data)
        return e
    async def get_trade_privacy(self):
        e = await request(url=f"https://accountsettings.roblox.com/v1/private-message-privacy", method='get',
                          cookies=self.cookies)
        return e['tradePrivacy']
    async def change_trade_privacy(self,privacy):
        data = {'tradePrivacy':privacy}
        e = await request(url=f"https://accountsettings.roblox.com/v1/private-message-privacy", method='post',
                          cookies=self.cookies,data=data)
        return e
    async def claim_group(self,grp_id:int):
        r = await request(url=f'https://groups.roblox.com/v1/groups/{grp_id}/claim-ownership',method='post',cookies=self.cookies)
        return r
    async def set_primary_group(self,grp_id:int):
        data = {
        "groupId": grp_id}

        r = await request(url='https://groups.roblox.com/v1/user/groups/primary',cookies=self.cookies,data=data,method='post')
        return r
    async def delete_primary_group(self):

        r = await request(url='https://groups.roblox.com/v1/user/groups/primary',cookies=self.cookies,method='delete')
        return r
    async def get_robux(self):
        r = await request(url=f"http://api.roblox.com/currency/balance",cookies=self.cookies,method='get')
        return r['robux']
    async def send_message(self,TargetId:int,subject:str,body:str):
        data = {
            'recipientid': TargetId,
            'subject': subject,
            'body': body
        }
        r = await request(url='https://www.roblox.com/messages/send', method='post', data=data,cookies=self.cookies)
        return r


    # TODO: get friend request
