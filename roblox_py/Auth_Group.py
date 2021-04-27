from .GroupInfo import GroupInfo
from .Classes import PartialInfo
from .utils import Requests


class GroupAuth:

    def __init__(self, request: Requests, groupID: int):
        """
        Represents a authenticated Group.

         **Parameters**
        ----------
        request : roblox_py.Requests
            Request class to request from
        groupID : int
            Group Id
        """
        self.request = request
        self.Target_grp_id = groupID

    async def group_info(self) -> GroupInfo:
        """ Returns Group Info class which contains more info about the group

            **Returns**
            -------
            roblox.py.GroupInfo
        """
        group = GroupInfo(groupID=self.Target_grp_id, request=self.request)
        await group.update()
        return group

    async def pay(self, user_id: int, amount: int):
        """ Pays the user robux from the group

        **Parameters**
        ----------
        user_id : int
            User's id to pay
        amount : int
            Amount to pay

        """
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
        r = await self.request.request(url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/payouts',
                                       data=data, method="post")
        return r

    async def change_description(self, description: str = None):
        """ Changes group description

        **Parameters**
        ----------
        description : str
            New description

         """
        data = {"description": description}
        e = await self.request.request(url=f"https://groups.roblox.com/v1/groups/{self.Target_grp_id}/description",
                                       method='patch', data=data)
        return e

    async def change_shout(self, status: str = None):
        """ Posts a new group shout

        **Parameters**
        ----------
        status : str
            New shout

        """
        data = {"message": status}
        e = await self.request.request(url=f"https://groups.roblox.com/v1/groups/{self.Target_grp_id}/status",
                                       method='patch', data=data)
        return e

    async def decline_join_request(self, user_id: int):
        """ Declines user join request

        **Parameters**
        ----------
        user_id : int
            User id
        """

        data = {"UserIds": [user_id]}
        e = await self.request.request(url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/join-requests',
                                       method='delete', data=data)
        return e

    async def accept_join_request(self, user_id: int):
        """ Accepts user join request

        **Parameters**
        ----------
        user_id : int
            User id
        """

        data = {"UserIds": [user_id]}
        e = await self.request.request(url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/join-requests',
                                       method='post', data=data)
        return e

    async def pay_percentage(self, user_id: int, percent: int):
        """ Pays the user robux percentage from the group

        **Parameters**
        ----------
        user_id : int
            User's id to pay
        percent : int
            Amount to pay robux percentage

        """
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
        r = await self.request.request(url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/payouts',
                                       data=data, method="post")
        return r

    async def change_rank(self, user_id: int, roleId: int):
        """ Changes a user Role

        **Parameters**
        ----------
        user_id : int
            User's id to pay
        roleId : int
           New role id

        """

        data = {
            'roleId': roleId
        }
        r = await self.request.request(url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/users/{user_id}',
                                       method="patch", data=data)
        return r

    async def get_funds(self) -> int:
        """ Gets Group's funds

        **Returns**
        -------
        int
            Group's Robux

        """
        r = await self.request.request(url=f'https://economy.roblox.com/v1/groups/{self.Target_grp_id}/currency',
                                       method='get')
        return r['robux']

    async def change_owner(self, user_id: int):
        """ Changes Group Owner


        **Parameters**
        ----------
        user_id : int
            User id

        """
        data = {"userId": user_id}
        r = await self.request.request(url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/change-owner',
                                       method='post',
                                       data=data)
        return r

    async def exile(self, user_id: int):
        """
        Removes User from a group

        **Parameters**
        ----------
        user_id : int
            User's id to remove
        """
        r = await self.request.request(url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/users/{user_id}',
                                       method='delete')
        return r

    async def get_social_link(self) -> dict:
        """
        Gets social links of the group

        **Returns**
        -------
        dict
            Dict  containing all social links

        """
        r = await self.request.request(
            url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/social-links',
            method='get')
        return r['data'][0]

    async def change_social_link(self, social_type: str, url: str, title: str):
        """
        Posts a Social link

        **Parameters**
        ----------
        social_type : str
            Social link type (i.e facebook,twitter)
        url : str
            Social Media link
        title : str
            Social Media Title
        """
        data = {
            "type": social_type,
            "url": url,
            "title": title
        }
        r = self.request.request(
            url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/social-links',
            method='post',
            data=data)
        return r

    async def delete_all_post(self, user_id: int):
        """
        Removes all post from the user

        **Parameters**
        ----------
        user_id : int
            User's id to remove posts
        """
        r = await self.request.request(
            url=f'https://groups.roblox.com/v1/groups/{self.Target_grp_id}/wall/users/{user_id}/posts', method='delete')
        return r

    async def exile_and_remove_posts(self, user_id: int):
        """
        Removes all posts from the user & exiles him

        **Parameters**
        ----------
        user_id : int
            ID of the user
        """
        remove_res = await self.delete_all_post(user_id=user_id)
        exile_user = await self.exile(user_id=user_id)
        return exile_user, remove_res

    async def get_roles_info(self) -> list:
        """
        Gets group's role info (ID,name)
        """
        link = f"https://groups.roblox.com/v1/groups/{self.Target_grp_id}/roles"
        res = await self.request.request(url=link, method='get')
        _list = []
        for stuff in res['roles']:
            name = stuff.get('name')
            role_id = stuff.get('id')
            inst = PartialInfo(name=name, id=role_id)
            _list.append(inst)
        return _list

    # TODO: get join request
