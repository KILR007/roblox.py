from .Classes import PartialInfo
from .exceptions import GameNotFound
import datetime
from .Classes import Time
class PlaceInfo:
    def __init__(self,universe_id,request):
        self.request = request
        self.universe_id = universe_id
        self._json_obj =  None
    async def update(self):
        r = await self.request.request(url=f'https://games.roblox.com/v1/games?universeIds={self.universe_id}')
        if 'rootPlaceId' not in r['data'][0]:
            raise GameNotFound()
        self._json_obj = r

    def id(self):
        return self._json_obj['data'][0]['rootPlaceId']

    @property
    def name(self):
        return self._json_obj['data'][0]['name']

    @property
    def description(self):
        return self._json_obj['data'][0]['description']

    @property
    def creator(self):
        if self._json_obj['data'][0]['creator']['type'] == 'User':
            return PartialInfo(id=self._json_obj['data'][0]['creator']['id'],name=self._json_obj['data'][0]['creator']['name'])

        elif self._json_obj['data'][0]['creator']['type'] == 'Group':
            return PartialInfo(id=self._json_obj['data'][0]['creator']['id'],name=self._json_obj['data'][0]['creator']['name'])
    @property
    def price(self):
        return self._json_obj['data'][0]['price']

    @property
    def allowed_gear_genres(self):
        return self._json_obj['data'][0]['allowedGearGenres']

    @property
    def allowed_gear_categories(self):
        return self._json_obj['data'][0]['allowedGearCategories']
    @property
    def playing(self):
        return self._json_obj['data'][0]['playing']

    @property
    def visits(self):
        return self._json_obj['data'][0]['visits']

    @property
    def max_players(self):
        return self._json_obj['data'][0]['maxPlayers']

    @property
    def created(self):
        return self._json_obj['data'][0]['created']

    @property
    def updated(self):
        return self._json_obj['data'][0]['updated']


    def updated_age(self):
        date_time_str = self.updated
        noob = date_time_str[:10]
        strp = datetime.datetime.strptime(noob, '%Y-%m-%d')
        now = datetime.datetime.utcnow()
        diff = now - strp
        days = diff.days
        months, days = divmod(days, 30)
        yrs, months = divmod(months, 12)
        return Time(yrs=yrs, month=months, day=days)
    def created_age(self):
        date_time_str = self.created
        noob = date_time_str[:10]
        strp = datetime.datetime.strptime(noob, '%Y-%m-%d')
        now = datetime.datetime.utcnow()
        diff = now - strp
        days = diff.days
        months, days = divmod(days, 30)
        yrs, months = divmod(months, 12)
        return Time(yrs=yrs, month=months, day=days)
    @property
    def create_vip_servers_allowed(self):
        return self._json_obj['data'][0]['createVipServersAllowed']
    @property
    def genre(self):
        return self._json_obj['data'][0]['genre']
    @property
    def api_access(self):
        return self._json_obj['data'][0]['studioAccessToApisAllowed']
    @property
    def universe_avatar_type(self):
        return self._json_obj['data'][0]['universeAvatarType']
    async def thumbnail(self):
        r = await self.request.request(url=f'https://thumbnails.roblox.com/v1/games/icons?universeIds={self.universe_id}&returnPolicy=PlaceHolder&size=512x512&format=Png&isCircular=false',method='get')
        return r['data'][0]['imageUrl']



