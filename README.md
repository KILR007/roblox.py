
# **pyrblx**

pyrblx Is An API Wrapper Written In Python For [Roblox](https://en.wikipedia.org/wiki/Roblox)

[![Support Server](https://img.shields.io/discord/591914197219016707.svg?label=Discord&logo=Discord&colorB=7289da&style=for-the-badge)](https://discord.gg/vpEv3HJ) [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/KILR007/pyrblx/blob/master/LICENSE.txt)


#### [PIP INSTALLATION](https://pypi.org/project/pyrblx/)
`pip install pyrblx`
(you are request to not to dowload this library cuz this library might get discontinue )


###  Quick Examples
````python
import pyrblx 
try:
    epic = pyrblx.PlayerInfo("kilr007") #Takes Name Of User
    print(epic.created_at)
    print(epic.description)
    print(epic.friends.name)
except pyrblx.PlayerNotFound:
    print("User Not Found")
             # or u can get the info by using the player ID
try:
    epic = pyrblx.PlayerInfo.get_by_id(925355805) #Takes ID Of User (Classmethod)
    print(epic.get_private_games)
    print(epic.account_age)
    print(epic.primary_group)
except pyrblx.PlayerNotFound:
    print("User Not Found")
````
#### Possible Attributes aka so called "Docs"-
# Player Info
````yaml
PlayersInfo  (Class)
id - Returns ID Of The User 
name - Returns The username of the user
description - Returns description
created_at - Returns Join Date
get_private_games - Returns a list of the user **private** games
oldest_private_game - Returns dict of oldest private game of user (ID + NAME) [use Assetinfo to get info of the game]
latest_private_game -  Returns dict of latest private game of user (ID + NAME) [use Assetinfo to get info of the game]
account_age - Returns account age of the user
direct_url - Returns dicret url aka roblox url of the user
avatar - Returns the avatar picture
thumbnail -  Returns the thumbnail picture 
````
````
friends (Class)
friends.name -  returns list of user's friends
friend.latest -  returns latest friend name
friends.count -  returns count of user
friends.oldest -  returns oldest friend name
````
````
following (Class)
following.name -  returns list of user's of people, user following
following.latest -  returns latest following name
following.count -  returns count of user following
following.oldest -  returns oldest following name
````
````
followers (Class)
followers.name -   returns list of user's followers
followers.latest -  returns latest follower name
followers.count -  returns count of user followers
followers.oldest -  returns oldest follower name
````
````
groups (Class)
groups.name -  returns list of user's joined Group
groups.latest -  returns latest group name
groups.count -  returns count of user Group
groups.oldest -  returns oldest group name
````

# Group Info

````
GroupInfo
enemies() - Returns List Of Group Enemies
allies() -  Returns List Of Group Allies
name() - Returns Group's Name
owner() - Returns Group's Owner Name
group_owner_id() -  Returns Group's Owner ID
count() -  Returns Group's Member Count
is_private() - Returns A Boolean 
is_premium_only_entry - 
shout() - Returns The Group's Shout
shout_poster() - Returns The Group's Shout Author Name
thumbnail() -  Returns Group's Thumbnail
direct_url() - Returns Group Roblox Url
description() - Returns Group's Description
members -  self-explainatory
latest_member - self-explainatory
oldest_member -  self-explainatory
games -  self-explainatory
private_games - self-explainatory
public_games -  self-explainatory
latest_game -  self-explainatory
oldest_game -  self-explainatory
oldest_private_game -  self-explainatory
latest_public_game -  self-explainatory
oldest_public_game -  self-explainatory
````


Bundles
name() - Returns The Bundle Name
id()  - returns id
description() - Returns The Bundle Description
bundle_creator() - Returns The Bundle Creator Name
price() - Return The Price Of The Bundle In Robux
Isforsale() - Returns A Boolean
type() - Returns The Type Of Bundle
direct_url - 
````


````
will be written later
```




#### Exceptions 
`BadArgument` -  Raised When The Site Return Status Code Other Than 200    
`BundleNotFound` - Raised When Group ID Is Invalid aka Not Found  
`GroupNotFound` - Raised When Bundle ID Is Invalid aka Not Found  
`PlayerNotFound` - Raised When Player Username Is Invalid aka Not Found  
`AssetNotFound`  -  Raised When Asset ID is invalid aka not Found
````





# TODO LIST 
- Improve Code Speed
- Write Better Docs Ofc
- Improve Code quality
#### Other
*This Library Is Still In Development*














