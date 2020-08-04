# **pyrblx**


pyrblx Is An API Wrapper Written In [Python](https://www.python.org/) For [Roblox](https://www.roblox.com)
#### PIP INSTALLATION
``pip install pyrblx``
###  Quick Examples
````python
import pyrblx 
try:
    epic = pyrblx.Players("kilr007") #Takes Name Of User
    print(epic.roblox_badges())
    print(epic.latest_friend())
    print(epic.groups_count())
except:
    pyrblx.Playernotfound:
    print("User Not Found")

````
#### Possible Attributes-
````python
Players
user_id() - Returns UserID
description() - Returns description
created_at() - Returns Join Dat
roblox_badges() - Returns List Of User's Roblox Badge
url() - Returns User's Roblox Profile URL
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
`Badarguement` -  Raised When The Site Return Status Code Other Than 200  
`Groupnotfound` - Raised When Group ID Is Invalid aka Not Found  
`Bundlenotfound` - Raised When Bundle ID Is Invalid aka Not Found 
`Playernotfound` - Raised When Player Username Is Invalid aka Not Found  


#### Other
*This Library Is Still In Development*














