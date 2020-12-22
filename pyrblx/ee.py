


from Player import PlayerInfo
from Groups import GroupInfo
from Asset import AssetInfo
import asyncio
from Client import Client

client = Client(cookies='28A7D0A4A36D22BA5B688E0952708C221999C2BA1DD1F0826174554B972DBC75B276BEBAB86FE85D4BA094F26C7CE74B31FD86375DDEFC4448CCD9ABD9F71E152D23053FE3B4D203A62028B5321D5A8A0B0067A8AC9945CE36A3813CAD27B68B44E3A7EFD4732DAA2F1EA56036630F0FF6442192DB2A22ED5BBF19E32FE003F451B21935CEB4CD809B7819A84D3968EBCB01E958D51C66680B2FCF0DE5191547BC659478E858AFE6688A83848CED437259A1588EBD091097096A0B18685A9021EEC0F50D46ED78F7086F670CE6C854A75685436263B37400BE8195E6E068A1A41BD3ECDC92B96287F0EF4B630D1CA5C04ECAE625675DF1CDB884D06D1F1A15C34F510DBCF450C295BF77B66E5A5C1E1DF4339D70CEC23DB03FECE2E346B4787BAFD6B3D1')
print(client.cookies)
async def main():
    '''
    pp = await GroupInfo(5948630)

    print(pp.name)
    print(await pp.enemies)
    print(await pp.allies)
    print(pp.id)
    print(pp.owner)
    print(pp.owner_id)
    print(pp.is_private)
    print(pp.is_premium_only_entry)
    print(pp.shout)
    print(pp.shout_poster)
    print(await pp.thumbnail)
    print(pp.description)
    print(await pp.direct_url)
    print(await pp.private_games)
    print(await pp.oldest_private_game)


    pp = await AssetInfo(537413528)
    print(pp.name)
    print(pp.id)
    print(pp.product_type)
    print(pp.creator_type)
    print(pp.description)
    print(pp.created_at)
    print(pp.created_age)
    print(pp.updated_at)
    print(pp.update_age)
    print(pp.sales)
    print(pp.buyable)

    print(pp.name)
    print(pp.id)
    print(pp.description)
    print(pp.account_age)
    print(pp.created_at)
    #print(await pp.get_private_games)
    print(await pp.thumbnail)
    print(await pp.avatar)
     pp = await PlayerInfo('kilr007')

    e = await pp.friends
    print(e.name)
    f = await pp.badges
    #print(await f.badges)
    ee = await pp.groups
    print(ee.count)

    e = await client.get_player_by_name('kilr007')
    e = await client.get_player_info(e)
    print(e,'3')
    fr = await e.friends
    print(fr.name)
    follow = await e.following
    ee = await follow.name
    print(len(ee))
    gr = await e.groups
    print(gr.name)
    print(e)
    ok = await e.badges
    print(await ok.badges)
    '''
    user = await client.get_player_info(925355805)
    print(await user.follow())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())


#import robloxpy
#print(robloxpy.SetCookie("2332323").red)