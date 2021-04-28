"""
<h1>
	<strong>roblox.py</strong>
</h1>
<p>
	<a href="https://discord.gg/vpEv3HJ">
		<img src="https://img.shields.io/discord/591914197219016707.svg?label=Discord&amp;logo=Discord&amp;colorB=7289da&amp;style=for-the-badge" alt="Support Server" />
	</a>
	<a href="https://github.com/KILR007/pyrblx/blob/master/LICENSE.txt">
		<img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT license" />
	</a>
	<a href="https://static.pepy.tech/badge/roblox.py">
		<img src="https://static.pepy.tech/badge/roblox.py" alt="Downloads" />
	</a>
	<br />
	<strong>Modern async API wrapper for Roblox with game client support</strong>
</p>
"""

from .exceptions import *
from .GamepassInfo import GamepassInfo
from .Auth_Group import GroupAuth
from .Client import Client
from .GroupInfo import *
from .PlayerInfo import *
from .BundleInfo import BundleInfo
from .AssetInfo import AssetInfo
from .Auth_Player import PlayerAuth
from .http_session import Http
from .utils import Requests
from .Twocaptcha import TwoCaptcha
__title__ = 'roblox_py'
__author__ = 'KILR'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021 KILR'
__version__ = '0.2.4'
