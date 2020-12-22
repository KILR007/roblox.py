
from .utis import send_request,request



class GroupAuth:
    def __init__(self,Target_grp_id:int,cookies=None):
        self.cookies = cookies
        self.Target_grp_id = Target_grp_id

    async def pay(self, user_id: int, amount: int):

        data = {
            "PayoutType": "FixedAmount",
            "Recipients": [
                {
                    "recipientId": user_id,
                    "recipientType": "User",
                    "amount": amount
                }
            ]
        }
        r = await request(url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/payouts', data=data,method="post")
        return r
    async def change_description(self,desc=None):
        data = {"description": desc}
        e = await request(url=f"https://groups.roblox.com/v1/groups/1/description",method='patch',data=data,cookies=self.cookies)
        return e

    async def change_shout(self, status=None):
        data = {"message": status}
        e = await request(url=f"https://groups.roblox.com/v1/groups/1/status", method='patch', data=data,
                          cookies=self.cookies)
        return e
    async def decline_join_request(self,user_id:int):
        data = {"UserIds": [user_id]}
        e = await send_request(url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/join-requests',method='delete',data=data)
        return e

    async def accept_join_request(self, user_id: int):
        data = {"UserIds": [user_id]}
        e = await send_request(url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/join-requests',
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
        r = await request(url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/payouts', data=data,method="post")
        return r

    async def set_rank(self, user_id: int, rank_id: int) -> int:
        """
        Set a users rank in the group.
        :param user_id: The users id
        :param rank_id: The rank id
        :return: StatusCode
        """
        data = {
            'roleId': rank_id
        }
        r = await request(url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/users/{user_id}',
                                       method="patch", data=data,cookies=self.cookies)
        return r
    async def get_funds(self):
        r = await request(url=f'https://economy.roblox.com/v1/groups/{self.Target_grp_id}/currency', method='get',cookies=self.cookies)
        return r
    # TODO: get join request