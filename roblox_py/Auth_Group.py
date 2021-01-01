

class GroupAuth:
    def __init__(self,request,groupID:int):
        self.request = request
        idkdd = isinstance(groupID, str)
        if idkdd:
            raise TypeError(f"{groupID} must be an integer")
        self.Target_grp_id = groupID

    async def pay(self, TargetId: int, amount: int):

        data = {
            "PayoutType": "FixedAmount",
            "Recipients": [
                {
                    "recipientId": TargetId,
                    "recipientType": "User",
                    "amount": amount
                }
            ]
        }
        r = await self.request.request(url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/payouts', data=data,method="post")
        return r
    async def change_description(self,description=None):
        data = {"description": description}
        e = await self.request.request(url=f"https://groups.roblox.com/v1/groups/{self.Target_grp_id}/description",method='patch',data=data)
        return e

    async def change_shout(self, status=None):
        data = {"message": status}
        e = await self.request.request(url=f"https://groups.roblox.com/v1/groups/1/status", method='patch', data=data)
        return e
    async def decline_join_request(self,user_id:int):
        data = {"UserIds": [user_id]}
        e = await self.request.request(url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/join-requests',method='delete',data=data)
        return e

    async def accept_join_request(self, user_id: int):
        data = {"UserIds": [user_id]}
        e = await self.request.request(url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/join-requests',
                                       method='post', data=data)
        return e

    async def pay_percentage(self, user_id: int, percent: int):

        data = {
            "PayoutType": "FixedAmount",
            "Recipients": [
                {
                    "recipientId": user_id,
                    "recipientType": "User",
                    "amount": percent
                }
            ]
        }
        r = await self.request.request(url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/payouts', data=data,method="post")
        return r

    async def change_rank(self, TargetId: int, rank_id: int):
        data = {
            'roleId': rank_id
        }
        r = await self.request.request(url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/users/{TargetId}',
                                       method="patch", data=data)
        return r
    async def get_funds(self):
        r = await self.request.request(url=f'https://economy.roblox.com/v1/groups/{self.Target_grp_id}/currency', method='get')
        return r['robux']
    async def change_owner(self,user_id:int):
        data = {"userId": user_id}

        r = await self.request.request(url=f'https://groups.roblox.com/v1/groups/4680721/change-owner',method='post',
                                       data=data)
        return r
    async def exile(self,user_id:int):
        r =  await self.request.request(url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/users/{user_id}',method='delete')
        return r
    async def get_social_link(self):
        r = self.request.request(url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/social-links',method='get')
        return r['data'][0]
    async def change_social_link(self,type:str,url:str,title:str):
        data = {
                "type": type,
                "url": url,
                "title": title}
        r = self.request.request(url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/social-links',method='post',data=data)
        return r
    async def delete_all_post(self,user_id:int):
        r = await self.request.request(url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/wall/users/{user_id}/posts',method='delete')
        return r
    # TODO: get join request
