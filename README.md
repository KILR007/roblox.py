
# **roblox.py**

Modern async API wrapper for Roblox  
[![Support Server](https://img.shields.io/discord/591914197219016707.svg?label=Discord&logo=Discord&colorB=7289da&style=for-the-badge)](https://discord.gg/vpEv3HJ)  [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/KILR007/pyrblx/blob/master/LICENSE.txt)[![Downloads](https://static.pepy.tech/badge/roblox.py)](https://static.pepy.tech/badge/roblox.py)



#### [PIP INSTALLATION](https://pypi.org/project/roblox.py/)
`pip install roblox.py`


###  Quick Examples
#### Playerinfo example
````python
import asyncio
from roblox_py import Client
client = Client() 
async def main():
    user = await client.get_user_info(925355805) # User Id here
    print(await user.friends)
    print(user.name)
    print(user.created_at)
    print(await user.promotion_channel)
    print(await user.following_count)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```` 
#### Groupinfo example

````python
import asyncio
from roblox_py import Client
client = Client() 
async def main():
    group = await client.get_group_info(4680721) # Group Id here
    print(await group.allies)
    print(group.name)
    print(group.owner)
    print(await group.enemies)
    print(await group.games)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```` 
#### Authenticated User Example
````python
import asyncio
from roblox_py import Client
client = Client(cookies="Your Cookies here") 
async def main():
    auth_user = await client.get_auth_user()
    await auth_user.follow(TargetId=1) # input user ID
    await auth_user.send_friend_request(TargetId=2) # input user ID 
    await auth_user.claim_group(2323) # clamins group if possible
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
````
#### Authenticated User Group Example

````python
import asyncio
from roblox_py import Client
client = Client(cookies="Your Cookies here") 
async def main():
    auth_group = await client.get_auth_group(3232) # group id of which u wanna take actions with
    await auth_group.pay(TargetId=1,amount=23) # Pays 23 robux to the user with the spcified user_id
    await auth_group.change_description(description="very cool description") 
    print(await auth_group.get_funds())
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
````
##### *For more example see Example Folder*


# TODO LIST 
- Improve Code Speed  
- Write  Docs (ofc)  
- Improve Code quality  
- PEP8 Code  

# Important Links
- Docs (not made yes see example folder)  
- [Examples](https://github.com/KILR007/roblox.py/tree/master/Examples)  
- [Discord Server](https://discord.gg/vpEv3HJ)  
- [Github](https://github.com/KILR007/roblox.py)  

### Note - 
*docs is not written yet, the upcomming updates might include breaking code changes, so please consider joining discord support server*









