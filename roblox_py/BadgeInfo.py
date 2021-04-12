from .exceptions import BadgeNotFound
from .PlaceInfo import PlaceInfo
import datetime
from .Classes import Time


class BadgeInfo:
    """
    Represents a ROBLOX Badge.
    
    """

    def __init__(self, badge_id, request):
        self.request = request
        self.badge_id = badge_id
        self._json_obj = None

    async def update(self):
        r = await self.request.request(url=f'https://badges.roblox.com/v1/badges/{self.badge_id}', method='get')
        if "id" not in r:
            raise BadgeNotFound("Invalid BadgeInfo ID")
        self._json_obj = r

    @property
    def name(self):
        return self._json_obj['name']

    @property
    def id(self):
        return self._json_obj['id']

    @property
    def description(self):
        return self._json_obj['description']

    @property
    def is_enabled(self):
        return self._json_obj['enabled']

    @property
    def created(self):
        return self._json_obj['created']

    @property
    def updated(self):
        return self._json_obj['updated']

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
    def past_day_awarded_count(self):
        return self._json_obj['statistics']['pastDayAwardedCount']

    @property
    def total_awarded_count(self):
        return self._json_obj['statistics']['awardedCount']

    @property
    def win_rate(self):
        return self._json_obj['statistics']['winRatePercentage']

    @property
    def game(self):
        return PlaceInfo(universe_id=self._json_obj['awardingUniverse']['id'], request=self.request)

    async def thumbnail(self):
        r = await self.request.request(
            url=f'https://thumbnails.roblox.com/v1/badges/icons?badgeIds={self.id}&size=150x150&format=Png&isCircular=false')
        return r['data'][0]['imageUrl']
