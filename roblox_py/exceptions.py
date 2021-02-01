
class NotFound(Exception):
    """ Not Found """
    pass

class PlayerNotFound(NotFound):
    """ Raised When Player  Not Found"""

class GamePassNotFound(NotFound):
    """ Raised When GamePass  Not Found"""


class GroupNotFound(NotFound):
    """ Raised When Group  Not Found"""

class BundleNotFound(NotFound):
    """ Raised When Bundle  Not Found"""

class BadgeNotFound(NotFound):
     """ Raised When Badge  Not Found"""
class GameNotFound(NotFound):
     """ Raised When Bundle  Not Found"""

class AssetNotFound(NotFound):
    """ Raised When Asset Is Not Found"""
class NotAuthenticated(Exception):
    """ Raised When User Not Authenticated"""
class HttpException(Exception):
    """ Http Error """
    pass
class InternalServiceError(HttpException):
    """500 HTTP error"""
    pass
class Unauthorized(HttpException):
    """401 HTTP error"""
    pass
class Forbidden(HttpException):
    """403 HTTP error"""
    pass
class RateLimited(HttpException):
    """429 HTTP error"""
    pass
class ServiceUnavailable(HttpException):
     """503 HTTP error"""
    pass
class UnknownError(HttpException):
    """ Unknown Error """
    pass
class BadRequest(NotFound):
    pass

class Captcha(Exception):
	""" Captcha Errors """
    pass

class InvalidAPIToken(Captcha):
	"""Raised when the 2captcha api key is invalid"""
    pass
class InsufficientCredit(Captcha):
	"""Raised when there is insufficient credit in 2captcha"""
    pass
class NoAvailableWorkers(Captcha):
	"""Raised when there are no available workers"""
    pass
