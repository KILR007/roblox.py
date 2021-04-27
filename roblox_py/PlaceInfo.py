from .Classes import PartialInfo
from .exceptions import GameNotFound
import datetime
from .Classes import Time
from .utils import Requests


class PlaceInfo:

    def __init__(self, universe_id: int, request: Requests):
        """
        Represents a ROBLOX Place.

        **Parameter**
        -------------

        universe_id : int
            Universe ID

        request : roblox_py.Requests
            Requests Class to do to HTTP requests
        """
        self.request = request
        self.universe_id = universe_id
        self._json_obj = None

    async def update(self):
        """
        Must be called before using the class else the class will misbehave.
        """
        r = await self.request.request(url=f'https://games.roblox.com/v1/games?universeIds={self.universe_id}')
        if 'rootPlaceId' not in r['data'][0]:
            raise GameNotFound()
        self._json_obj = r

    def id(self) -> int:
        """

        Returns Place's ID

         """
        return self._json_obj['data'][0]['rootPlaceId']

    @property
    def name(self) -> str:
        """

        Returns Place's Name

         """
        return self._json_obj['data'][0]['name']

    @property
    def description(self) -> str:
        """

        Returns Place's Description

         """
        return self._json_obj['data'][0]['description']

    @property
    def creator(self) -> PartialInfo:
        """
        Returns a partial info instance which contains the Place creator's name and ID.
        """
        if self._json_obj['data'][0]['creator']['type'] == 'User':
            return PartialInfo(
                id=self._json_obj['data'][0]['creator']['id'],
                name=self._json_obj['data'][0]['creator']['name'])

        elif self._json_obj['data'][0]['creator']['type'] == 'Group':
            return PartialInfo(
                id=self._json_obj['data'][0]['creator']['id'],
                name=self._json_obj['data'][0]['creator']['name'])

    @property
    def price(self) -> int:
        """
        Returns Bundle Price( 0 if free)
        """
        return self._json_obj['data'][0]['price']

    @property
    def allowed_gear_genres(self) -> list:
        """
        Returns all the allowed Gear Genres
        """
        return self._json_obj['data'][0]['allowedGearGenres']

    @property
    def allowed_gear_categories(self) -> list:
        """
        Returns all the allowed Gear Categories
        """
        return self._json_obj['data'][0]['allowedGearCategories']

    @property
    def number_of_playing(self) -> int:
        """
        Gets the number of people playing the game
        """
        return self._json_obj['data'][0]['playing']

    @property
    def visits(self) -> int:
        """
        Gets Number of Visits
        """
        return self._json_obj['data'][0]['visits']

    @property
    def max_players(self) -> int:
        """
        Gets the  maximum capacity of server
        """
        return self._json_obj['data'][0]['maxPlayers']

    @property
    def created_at(self) -> str:
        """
        Gives the created date in iso8601 format
        """
        return self._json_obj['data'][0]['created']

    @property
    def updated_at(self) -> str:
        """
        Gives the last updated date in iso8601 format
        """
        return self._json_obj['data'][0]['updated']

    def updated_age(self) -> Time:
        """
        Returns a Time instance which contains the years, months, and days since the asset's last update.
        """
        date_time_str = self.updated_at
        noob = date_time_str[:10]
        strp = datetime.datetime.strptime(noob, '%Y-%m-%d')
        now = datetime.datetime.utcnow()
        diff = now - strp
        days = diff.days
        months, days = divmod(days, 30)
        yrs, months = divmod(months, 12)
        return Time(yrs=yrs, month=months, day=days)

    def created_age(self) -> Time:
        """
        Returns a Time instance which contains the years, months, and days since the Place created date.
        """
        date_time_str = self.created_at
        noob = date_time_str[:10]
        strp = datetime.datetime.strptime(noob, '%Y-%m-%d')
        now = datetime.datetime.utcnow()
        diff = now - strp
        days = diff.days
        months, days = divmod(days, 30)
        yrs, months = divmod(months, 12)
        return Time(yrs=yrs, month=months, day=days)

    @property
    def create_vip_servers_allowed(self) -> bool:
        """
        Checks if user is allowed to create vip servers or not
        """
        return self._json_obj['data'][0]['createVipServersAllowed']

    @property
    def genre(self) -> str:
        """
        Gives Place Genre
        """
        return self._json_obj['data'][0]['genre']

    @property
    def api_access(self) -> str:
        """
        Checks if the Game is  allowed to use APIs
        """
        return self._json_obj['data'][0]['studioAccessToApisAllowed']

    @property
    def universe_avatar_type(self) -> str:
        """
        Returns Universe Avatar Type
        """
        return self._json_obj['data'][0]['universeAvatarType']

    async def thumbnail(self) -> str:
        """
        Returns Place's Thumbnail image link
        """
        r = await self.request.request(
            url=f'https://thumbnails.roblox.com/v1/games/icons?universeIds={self.universe_id}'
                f'&returnPolicy=PlaceHolder&size=512x512&format=Png&isCircular=false',
            method='get')
        return r['data'][0]['imageUrl']
