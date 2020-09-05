

# **pyrblx**

pyrblx Is An API Wrapper Written In Python For [Roblox](https://www.roblox.com)

[![Support Server](https://img.shields.io/discord/591914197219016707.svg?label=Discord&logo=Discord&colorB=7289da&style=for-the-badge)](https://discord.gg/vpEv3HJ) [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/KILR007/pyrblx/blob/master/LICENSE.txt)


#### [PIP INSTALLATION](https://pypi.org/project/pyrblx/)
`pip install pyrblx`

###  Quick Examples
````python
import pyrblx 
try:
    epic = pyrblx.Players("kilr007") #Takes Name Of User
    print(epic.created_at())
    print(epic.description())
    print(epic.avatar())
except pyrblx.PlayerNotFound:
    print("User Not Found")
              #or
try:
    epic = pyrblx.Players.get_by_id(925355805) #Takes ID Of User (Classmethod)
    print(epic.roblox_badges())
    print(epic.latest_friend())
    print(epic.groups_count())
except pyrblx.PlayerNotFound:
    print("User Not Found")
````
#### Possible Attributes-
````text
Players
user_id() - Returns ID Of The User 
user_name() - Returns The username of the user
description() - Returns description
created_at() - Returns Join Dat
roblox_badges() - Returns List Of User's Roblox Badge
direct_url() - Returns User's Roblox Profile URL
friends() - Returns List Of User's Friend Name
latest_friend() - Returns User's Lastest Friend Name 
friends_count() - Returns Number Of Friend Of User
oldest_friend() - Returns User's Oldest Friend Name  
groups() - Returns List Of User's Groups Name
latest_group() -  Returns User's Latest Joined Group Name 
oldest_group() - Returns User's Oldest Joined Group Name 
groups_count() - Returns Number Of Groups Of User
thumbnail() -  Returns User's Thumbnail
avatar() - Returns User's Avatar



Groups
group_enemies() - Returns List Of Group Enemies
group_allies() -  Returns List Of Group Allies
group_name() - Returns Group's Name
group_owner_name() - Returns Group's Owner Name
group_owner_id() -  Returns Group's Owner ID
group_member_count() -  Returns Group's Member Count
is_private() - Returns A Boolean 
group_shout() - Returns The Group's Shout
group_shout_poster_name() - Returns The Group's Shout Author Name
group_thumbnail() -  Returns Group's Thumbnail
group_url() - Returns Group Roblox Url
group_description() - Returns Group's Description



Bundles
bundle_name() - Returns The Bundle Name
description() - Returns The Bundle Description
bundle_creator_name() - Returns The Bundle Creator Name
bundle_creator_id() - Returns The Bundle Creator ID
price() - Return The Price Of The Bundle In Robux
isforsale() - Returns A Boolean
type() - Returns The Type Of Bundle
````
#### Exceptions 
`BadArgument` -  Raised When The Site Return Status Code Other Than 200    
`BundleNotFound` - Raised When Group ID Is Invalid aka Not Found  
`GroupNotFound` - Raised When Bundle ID Is Invalid aka Not Found  
`PlayerNotFound` - Raised When Player Username Is Invalid aka Not Found  



#### Other
*This Library Is Still In Development*
