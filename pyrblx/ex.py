class BadArgument(Exception):
    """Raised When Site Return Status Code Other Than 200"""

class NotFound(Exception):
    pass

class PlayerNotFound(NotFound):
    """ Raised When Player Is Not Found"""


class GroupNotFound(NotFound):
    """ Raised When Group Is Not Found"""


class BundleNotFound(NotFound):
    """ Raised When Bundle Is Not Found"""


class AssetNotFound(NotFound):
    """ Raised When Bundle Is Not Found"""
class NotAuthenticated(Exception):
    """ Raised When User Not Authenticated"""
