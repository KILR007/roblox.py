

from .PlayerInfo import PlayerInfo
from .Classes import Time,AccountInformationMetaData,PromotionChannel
class PlayerAuth:
    def __init__(self,request):
        self.request = request
        

    async def get_self(self):
        e = await self.request.request(url=f'https://users.roblox.com/v1/users/authenticated',method='get')
        return PlayerInfo(playerID=e['id'],request=self.request)

    async def is_premium(self):
        e = await self.request.request(url=f'https://www.roblox.com/mobileapi/userinfo',method='get')
        return e['IsPremium']

    async def follow(self,TargetId:int):
        data = {
            'targetUserId': TargetId
        }
        e = await self.request.request(url=f'https://friends.roblox.com/v1/users/{TargetId}/follow',method='post',data=data)
        return e


    async def unfollow(self,TargetId:int):
        data = {
            'targetUserId': TargetId
        }
        e = await self.request.request(url=f'https://friends.roblox.com/v1/users/{TargetId}/unfollow',method='post',data=data)
        return e

    async def block(self,TargetId:int):
        e = await self.request.request(url=f'https://accountsettings.roblox.com/v1/users/{TargetId}/block',method='post')
        return e

    async def unblock(self,TargetId:int):
        e = await self.request.request(url=f'https://accountsettings.roblox.com/v1/users/{TargetId}/unblock', method='post',
                          )
        return e

    async def send_friend_request(self,TargetId:int):
        data = {
            'targetUserId': TargetId
        }
        e = await self.request.request(url=f'https://friends.roblox.com/v1/users/{TargetId}/request-friendship', method='post',
                          data=data)
        return e

    async def unfriend(self,TargetId:int):
        data = {
            'targetUserId': TargetId
        }
        e = await self.request.request(url=f'https://friends.roblox.com/v1/users/{TargetId}/unfriend', method='post',
                          data=data)
        return e

    async def friend_request_count(self):

        e = await self.request.request(url=f'https://friends.roblox.com/v1/user/friend-requests/count', method='get',
                          )
        return e['count']

    async def decline_request(self,TargetId:int):
        data = {
            'targetUserId': TargetId
        }
        e = await self.request.request(url=f'https://friends.roblox.com/v1/users/{TargetId}/decline-friend-request', method='post',
                          data=data)
        return e

    async def accept_request(self,TargetId:int):
        data = {
            'targetUserId': TargetId
        }
        e = await self.request.request(url=f'https://friends.roblox.com/v1/users/{TargetId}/accept-friend-request', method='post',
                          data=data)
        return e

    async def is_following(self,TargetId:int):
        data = {"targetUserIds": [TargetId]}
        e = await self.request.request(url=f'https://friends.roblox.com/v1/user/following-exists',
                          method='post',
                          data=data)
        return e['followings'][0]['isFollowing']

    async def get_birth_date(self):
        e = await self.request.request(url=f'https://accountinformation.roblox.com/v1/birthdate',method='get')
        return Time(yrs=e['birthYear'],month=e['birthMonth'],day=e['birthDay'])

    async def change_birth_day(self,day,month,year):
        data = {
        "birthMonth": month,
        "birthDay": day,
        "birthYear": year}
        e = await self.request.request(url=f'https://accountinformation.roblox.com/v1/birthdate',method='post',data=data)
        return e

    async def get_gender(self):
        e = await self.request.request(url='https://accountinformation.roblox.com/v1/gender',method='get')
        val = e['gender']
        if val == 2:
            gender = "Male"
        else:
            gender = "Female"
        return gender

    async def change_gender(self,gender):
        data = dict(gender=gender)
        e = await self.request.request(url='https://accountinformation.roblox.com/v1/gender',method='post',data=data)
        return e

    async def get_phone(self):
        e = await self.request.request(url='https://accountinformation.roblox.com/v1/phone',method='get')
        return e

    async def change_phone(self,code,prefix,phone,password):
        data = {
        "countryCode": code,
        "prefix": prefix,
        "phone": phone,
        "password": password
        }
        e = await self.request.request(url='https://accountinformation.roblox.com/v1/phone',method='post',data=data)
        return e

    async def metadata(self):
        e = await self.request.request(url=f'https://accountinformation.roblox.com/v1/metadata',method='get')
        return AccountInformationMetaData(iteam=e)

    async def delete_phone(self,code,prefix,phone,password):
        data = {
        "countryCode": code,
        "prefix": prefix,
        "phone": phone,
        "password": password
        }
        e = await self.request.request(url='https://accountinformation.roblox.com/v1/phone/delete',method='post',data=data)
        return e

    async def verify_phone(self,code):
        data = dict(code=code)
        e = await self.request.request(url='https://accountinformation.roblox.com/v1/phone/verify',method='post',data=data)
        return e

    async def get_promotion_channel(self):
        e = await self.request.request(url='https://accountinformation.roblox.com/v1/promotion-channels',method='get')
        return PromotionChannel(iteam=e)

    async def change_promotion_channel(self,**kwargs):
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

        e = await self.request.request(url='https://accountinformation.roblox.com/v1/phone/promotion-channels', method='post',
                          data=data,
                          )
        return e

    async def get_star_code(self):
        e = await self.request.request(url=f'https://accountinformation.roblox.com/v1/star-code-affiliates',method='get')
        return e

    async def change_star_code(self,code):
        data = {"code": code}
        e = await self.request.request(url=f'https://accountinformation.roblox.com/v1/star-code-affiliates',method='post',data=data)
        return e

    async def delete_star_code(self):
        e = await self.request.request(url=f'https://accountinformation.roblox.com/v1/star-code-affiliates', method='delete',
                          )
        return e

    async def get_chat_app_privacy(self):
        e = await self.request.request(url=f'https://accountsettings.roblox.com/v1/app-chat-privacy',method='get')
        return e['appChatPrivacy']

    async def change_chat_app_privacy(self,privacy):
        data = {
            "appChatPrivacy": privacy
        }
        e = await self.request.request(url=f'https://accountsettings.roblox.com/v1/app-chat-privacy',method='post',data=data)
        return e

    async def get_game_app_privacy(self):
        e = await self.request.request(url=f'https://accountsettings.roblox.com/v1/game-chat-privacy',method='get')
        return e['gameChatPrivacy']

    async def change_game_app_privacy(self,privacy):
        data = {
            "gameChatPrivacy": privacy
        }
        e = await self.request.request(url=f'https://accountsettings.roblox.com/v1/game-chat-privacy',method='post',data=data)
        return e

    async def get_inventory_privacy(self):
        e = await self.request.request(url=f'https://accountsettings.roblox.com/v1/inventory-privacy', method='get',
                          )
        return e['inventoryPrivacy']

    async def change_inventory_privacy(self, privacy):
        data = {
            "inventoryPrivacy": privacy
        }
        e = await self.request.request(url=f'https://accountsettings.roblox.com/v1/inventory-privacy', method='post',
                          data=data)
        return e

    async def get_private_message_privacy(self):
        e = await self.request.request(url=f"https://accountsettings.roblox.com/v1/private-message-privacy",method='get')
        return e['privateMessagePrivacy']

    async def change_private_message_privacy(self,privacy):
        data = {"privateMessagePrivacy": privacy}
        e = await self.request.request(url=f"https://accountsettings.roblox.com/v1/private-message-privacy",method='post',data=data)
        return e

    async def get_email(self):
        e = await self.request.request(url='https://accountsettings.roblox.com/v1/email',method='get')
        return e

    async def change_email(self,new_email,password):
        data = {"password": password,"emailAddress": new_email}
        e = await self.request.request(url='https://accountsettings.roblox.com/v1/email',method='post',data=data)
        return e

    async def get_trade_privacy(self):
        e = await self.request.request(url=f"https://accountsettings.roblox.com/v1/private-message-privacy", method='get',
                          )
        return e['tradePrivacy']

    async def change_trade_privacy(self,privacy):
        data = {'tradePrivacy':privacy}
        e = await self.request.request(url=f"https://accountsettings.roblox.com/v1/private-message-privacy", method='post',
                          data=data)
        return e

    async def claim_group_owner(self,grp_id:int):
        r = await self.request.request(url=f'https://groups.roblox.com/v1/groups/{grp_id}/claim-ownership',method='post')
        return r

    async def set_primary_group(self,grp_id:int):
        data = {
        "groupId": grp_id}
        r = await self.request.request(url='https://groups.roblox.com/v1/user/groups/primary',data=data,method='post')
        return r

    async def delete_primary_group(self):
        r = await self.request.request(url='https://groups.roblox.com/v1/user/groups/primary',method='delete')
        return r

    async def get_robux(self):
        r = await self.request.request(url=f"http://api.roblox.com/currency/balance",method='get')
        return r['robux']

    async def buy(self,product_id:int):
        ee = self.request.request(url=f'https://economy.roblox.com/v2/user-products/{product_id}/purchase',method='post')
        return ee
    async def change_username(self,new_username,password):
        data = {"username": f"{new_username}","password": f"{password}"}
        ee = await self.request.request(url=f'https://auth.roblox.com/v2/username',method='post',data=data)
        return ee
    # TODO: get friend request
    async def post_message_in_wall(self,group_id,message,captcha_token=None):
        data = {"body": f"{message}"}

        a = await self.request.just_request(url=f'https://groups.roblox.com/v2/groups/{group_id}/wall/posts',data=data,method='post')
        json_text = await a.json()
        if a.status == 403:
            if json_text['errors'][0]['message'] == "Captcha must be solved.":
                et = await captcha_token.solve(ckey=f'63E4117F-E727-42B4-6DAA-C8448E9B137F')
                data = {
                    "body": "string",
                    "captchaToken": f"{et}",
                    "captchaProvider": "PROVIDER_ARKOSE_LABS"}
                b = await self.request.just_request(url=f'https://groups.roblox.com/v2/groups/{group_id}/wall/posts',
                                                    data=data,method='post')
                jj = await b.json()
                return jj
        else:
            return json_text

    async def join_group(self,group_id,captcha_token=None):
        data = {}

        a = await self.request.just_request(url=f'https://groups.roblox.com/v1/groups/{group_id}/users', data=data, method='post')
        json_text = await a.json()
        print(json_text)
        if a.status == 403:
            if json_text['errors'][0]['message'] == "You must pass the captcha test before joining this group.":
                et = await captcha_token.solve(ckey=f'63E4117F-E727-42B4-6DAA-C8448E9B137F')
                data = {
                    "captchaToken": f"{et}",
                    "captchaProvider": "PROVIDER_ARKOSE_LABS"}
                b = await self.request.just_request(url=f'https://groups.roblox.com/v1/groups/{group_id}/users',
                                                    data=data, method='post')

                jj = await b.json()
                return jj
        else:
            return json_text

    async def redeem_gamecard(self,game_code,captcha_token):
        data = {"pinCode": f"{game_code}"}

        a = await self.request.just_request(url=f'https://billing.roblox.com/v1/gamecard/redeem', data=data,
                                            method='post')
        json_text = await a.json()
        if a.status == 403:
            if json_text['errors'][0]['message'] == "Captcha":
                et = await captcha_token.solve(ckey=f'1B154715-ACB4-2706-19ED-0DC7E3F7D855')
                data = {
                    "pinCode": f"{game_code}",
                    "captchaToken": f"{et}",
                    "captchaProvider": "PROVIDER_ARKOSE_LABS"}
                b = await self.request.just_request(url=f'https://billing.roblox.com/v1/gamecard/redeem',
                                                    data=data, method='post')

                jj = await b.json()
                return jj
        else:
            return json_text
