class AccountInformationMetaData:
    def __init__(self, item: dict):
        """

        Account Information Meta Data Class

        """

        self.is_account_settings_policy_enabled = item["isAccountSettingsPolicyEnabled"]
        self.is_phone_number_enabled = item["isPhoneNumberEnabled"]
        self.max_user_description_length = item["MaxUserDescriptionLength"]
        self.is_user_description_enabled = item["isUserDescriptionEnabled"]
        self.is_user_block_endpoints_updated = item["isUserBlockEndpointsUpdated"]


class PromotionChannel:
    """

    Promotion Channel Class

    """

    def __init__(self, **kwargs):
        self.channels_visibility_privacy = kwargs.get(
            "promotionChannelsVisibilityPrivacy")
        self.facebook = kwargs.get("facebook")
        self.twitter = kwargs.get("twitter")
        self.youtube = kwargs.get("youtube")
        self.twitch = kwargs.get("twitch")


class Time:
    """

    Time and Date Class

    """

    def __init__(self, yrs, month, day):
        """
        Parameters
        ----------
        yrs : int
            Name of the Object
        month : int
            ID of the Object
        day : int
            Date
        """
        self.years = yrs
        self.months = month
        self.days = day

    def __repr__(self):
        return f"{self.years}/{self.months}/{self.days}"


class PartialInfo:
    """

    Partial Info Class

    """

    def __init__(self, id, name):
        """
           Parameters
           ----------
           name : str
               Name of the Object
           id : int
               ID of the Object
        """

        self.id = id
        self.name = name

    def __repr__(self):
        return self.name


class UserPresences:
    """
    UserPresences Class
    """

    def __init__(self, **kwargs):
        self.presenceType = kwargs.get("userPresenceType")
        self.lastLocation = kwargs.get("lastLocation")
        self.placeId = kwargs.get("placeId")
        self.rootPlaceId = kwargs.get("rootPlaceId")
        self.universeId = kwargs.get("universeId")
        self.gameId = kwargs.get("gameId")
        self.userId = kwargs.get("userId")
        self.lastOnline = kwargs.get("lastOnline")
