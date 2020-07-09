# **pyroblox3**



pyroblox Is A library Written In [Python](https://www.python.org/)
  - Made For Finding [Roblox](https://www.roblox.com) Accounts(Info)
  - Very Easy To Use
###  Library Usage With Examples
```py
from pyroblox3 import Player
epic = Player(f"Kilr007") #Player Name Here 
Desc = epic.descrition()
avatar = epic.avatar()
created_at = epic.created()
print(created_at)
print(avatar)
print(Desc)
```
#### Possible Attributes-
```python
avatar() 
url()
badges()
created()
descrition()
id()
```
*If The User Don't Exist Each Attribute Will Return "User Not Found"*

### Documentation
`avatar()` -- For User Avatar Url  
`url()` --  For User Roblox Profile User  
`badges()` --  For User Roblox Badges  
`created()`-- For User Join Date  
`descrition()` --  For User Roblox Description  
`id()` --  For User Roblox ID  
### [Discord](https://discord.com) Example
This Module Is Very Useful When Your Creating A Discord Bot That Finds Roblox Account Info
###### Quick Example
```python
import discord
from discord.ext import commands
from Roblox import Player
@bot.command()
async def roblox(ctx,*,username):
    epic = Player(f"{username}")
    ee = epic.id()
    if ee == "User Not Found":
        await ctx.send("Account No Longer Exists Or It Is Banned") 
        return
         # If User Not Found Then Return With A Message
    embed = discord.Embed(color=discord.Color.green())
    embed.add_field(name="Username:", value=username)
    embed.add_field(name="Roblox Id", value=epic.id())
    embed.add_field(name="Account Created on:", value=epic.created())
    embed.add_field(name="Roblox Badges:", value=epic.badge())
    embed.add_field(name="Description:", value=epic.descrition(), inline=False)
    embed.add_field(name="Roblox Profile URL:", value="e", inline=False)
    embed.set_thumbnail(url=epic.avatar())
    await ctx.send(embed=embed)
```

### Other
 - If The User Don't Exist/Banned Each Attribute Will Return `User Not Found`
 - If User Don't Have A Description Then It Will Return `*No Description*`
 - If User Don't Have Any Roblox Badges Then It Will Return `*No Roblox Badges*`
 
**Note-** *This Library Is Still In Development*







`







