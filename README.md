# **pyrblx**


pyrblx Is A library Written In [Python](https://www.python.org/)
  - Made For Finding [Roblox](https://www.roblox.com) Accounts(Info)
  - Very Easy To Use
###  [Pip](https://pypi.org/project/pyrblx/) Installation

```pip install pyrblx```

###  Library Usage With Examples
```py
import pyrblx 
try:
    epic = pyrblx.Players(f"Kilr007") #Player Name Here 
    Desc = epic.description()
    avatar = epic.avatar()
    created_at = epic.created_at()
    print(created_at)
    print(avatar)
    print(Desc)
except pyrblx.PlayerNotFound:
    print("No Player Found")
```
#### Possible Attributes-
```python
avatar() 
url()
badges()
created_at()
description()
id()
```


### Documentation
`avatar()` -- For User Avatar Url  
`url()` --  For User Roblox Profile User    
`badges()` --  For User Roblox Badges   
`created()`-- For User Join Date  
`descrition()` --  For User Roblox Description    
`id()` --  For User Roblox ID 
   ##### Other
 - If User Don't Have A Description Then It Will Return `*No Description*`  
 - If User Don't Have Any Roblox Badges Then It Will Return`*No Roblox Badges*`  
 - If The User Don't Exist/Banned Library Will Raise `PlayerNotFound` Error  
 
### [Discord](https://discord.com) Example
This Module Is Very Useful When Your Creating A Discord Bot That Finds Roblox Account Info
###### Quick Example
```python
import discord
from discord.ext import commands
import pyrblx
@bot.command()
async def roblox(ctx,*,username):
    try:
        epic = pyrblx.Players(f"{username}")
        embed = discord.Embed(color=discord.Color.green())
        embed.add_field(name="Username:", value=username)
        embed.add_field(name="Roblox Id", value=epic.id())
        embed.add_field(name="Account Created on:", value=epic.created_at())
        embed.add_field(name="Roblox Badges:", value=epic.badge())
        embed.add_field(name="Description:", value=epic.description(), inline=False)
        embed.add_field(name="Roblox Profile URL:", value="e", inline=False)
        embed.set_thumbnail(url=epic.avatar())
        await ctx.send(embed=embed)
    except pyrblx.PlayerNotFound:
        return await ctx.send("No Player Found!")
```

*This Library Is Still In Development*














