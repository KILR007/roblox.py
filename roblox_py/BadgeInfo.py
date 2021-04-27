from .exceptions import BadgeNotFound
from .PlaceInfo import PlaceInfo
import datetime
from .Classes import Time
from .utils import Requests


class BadgeInfo:

    def __init__(self, badge_id, request: Requests):
        """

        Represents a ROBLOX Badge.

        **Parameter**
        -------------

        badge_id : int
            Badge Id
        request : roblox_py.Requests
        """
        self.request = request
        self.badge_id = badge_id
        self._json_obj = None

    async def update(self) -> None:
        """
        Must be called before using the class else the class will misbehave.
        """
        r = await self.request.request(url=f'https://badges.roblox.com/v1/badges/{self.badge_id}', method='get')
        if "id" not in r:
            raise BadgeNotFound("Invalid BadgeInfo ID")
        self._json_obj = r

    @property
    def name(self) -> str:
        """
        Returns Badge's Name

        """
        return self._json_obj['name']

    @property
    def id(self) -> int:
        """
        Returns Badge's ID
        """
        return self._json_obj['id']

    @property
    def description(self) -> str:
        """
        Returns Badge's Description
        """
        return self._json_obj['description']

    @property
    def is_enabled(self) -> bool:
        """
        Checks if the badge is enabled or not

        """

        return self._json_obj['enabled']

    @property
    def created_at(self) -> str:
        """
        Gives the created date in iso8601  format
        """
        return self._json_obj['created']

    @property
    def updated_at(self):
        """
        Gives the last updated date in iso8601 format
        """
        return self._json_obj['updated']

    def updated_age(self) -> Time:
        """
        Returns a Time instance which contains the years, months, and days since the badge's last update.
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
        Returns a Time instance which contains the years, months, and days the account has been up for.
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
    def past_day_awarded_count(self) -> int:
        """
        Returns amount of people awarded in past day
        """
        return self._json_obj['statistics']['pastDayAwardedCount']

    @property
    def total_awarded_count(self) -> int:
        """
        Returns total amount of people awarded
        """
        return self._json_obj['statistics']['awardedCount']

    @property
    def win_rate(self) -> float:
        """
        Returns Win-rate Ratio of the badge
        """
        return self._json_obj['statistics']['winRatePercentage']

    async def game(self) -> PlaceInfo:
        """
        Returns Place info instance which contains more info about the badge's game

        **Returns**
        -----------

        roblox_py.PlaceInfo
        """
        game = PlaceInfo(
            universe_id=self._json_obj['awardingUniverse']['id'],
            request=self.request)
        await game.update()
        return game

    async def thumbnail(self) -> str:
        """
        Returns the badge's thumbnail image link.
        """
        r = await self.request.request(
            url=f'https://thumbnails.roblox.com/v1/badges/icons?badgeIds={self.id}'
                f'&size=150x150&format=Png&isCircular=false')
        return r['data'][0]['imageUrl']
