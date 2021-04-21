class AccountInformationMetaData:
    def __init__(self, iteam):
        """

        Account Infomation Meta Data Class

        """

        self.is_account_settings_policy_enabled = iteam["isAccountSettingsPolicyEnabled"]
        self.is_phone_number_enabled = iteam["isPhoneNumberEnabled"]
        self.max_user_description_length = iteam["MaxUserDescriptionLength"]
        self.is_user_description_enabled = iteam["isUserDescriptionEnabled"]
        self.is_user_block_endpoints_updated = iteam["isUserBlockEndpointsUpdated"]


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
    month : str
        ID of the Object
    day : int
        Date
    """
        self.years = yrs
        self.months = month
        self.days = day


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
