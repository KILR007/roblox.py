class AccountInformationMetaData:
    def __init__(self, iteam):
        self.is_account_settings_policy_enabled = iteam["isAccountSettingsPolicyEnabled"]
        self.is_phone_number_enabled = iteam["isPhoneNumberEnabled"]
        self.max_user_description_length = iteam["MaxUserDescriptionLength"]
        self.is_user_description_enabled = iteam["isUserDescriptionEnabled"]
        self.is_user_block_endpoints_updated = iteam["isUserBlockEndpointsUpdated"]


class PromotionChannel:
    def __init__(self, **kwargs):
        self.channels_visibility_privacy = kwargs.get("promotionChannelsVisibilityPrivacy")
        self.facebook = kwargs.get("facebook")
        self.twitter = kwargs.get("twitter")
        self.youtube = kwargs.get("youtube")
        self.twitch = kwargs.get("twitch")


class Time:
    def __init__(self, yrs, month, day):
        self.years = yrs
        self.months = month
        self.days = day


class PartialInfo:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return self.name
