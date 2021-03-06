import os
import getpass
from .exceptions import *
import subprocess
from .utils import Requests


class JoinGame:

    def __init__(
            self,
            request: Requests,
            game_id: int,
            roblox_game_folder_path: str = None,
            roblox_folder_path: str = None):
        """
        Represents a Game Join class.

        **Parameters**
        --------------
        request : roblox_py.Requests
            Requests Class for HTTP Requests
        game_id : int
            Game ID to join
        roblox_game_path : str
            Folder which contains RobloxPlayerBeta.exe
        roblox_folder_path : str
            Roblox Folder Path which contains other roblox Stuff ( textures, storage dir)


        """
        if roblox_folder_path is None:
            self.main_game_path = f'C:/Users/{getpass.getuser()}/AppData/Local/Roblox'
        else:
            self.main_game_path = roblox_folder_path
        self.process = None
        self._id = game_id
        self.request = request
        # self.robloxLocalStoragePath = f'{self.main_game_path}/LocalStorage'
        # self.browser_track_id_path = f'{self.robloxLocalStoragePath}/appStorage.json'
        # self.version_path = f'{self.main_game_path}/Versions'
        # self.browser_track_id = None

        self.game_path = None
        templates = [

            "C:/Program Files (x86)/Roblox/Versions",
            "C:/Program Files/Roblox/Versions",
            f"C:/Users/{getpass.getuser()}/AppData/Local/Roblox/Versions",
        ]
        if roblox_game_folder_path is None:
            for a in templates:
                for root, dirs, files in os.walk(a):
                    for names in files:
                        if names.startswith("RobloxPlayerBeta"):
                            self.game_path = f"{root}"
        else:
            self.game_path = f"{roblox_game_folder_path}"

    async def get_roblox_auth_ticket(self):
        """

        Returns Roblox Auth Ticket

        """
        e = await self.request.return_headers(url="https://auth.roblox.com/v1/authentication-ticket/", method='post')
        return str(e['rbx-authentication-ticket'])

    async def check_if_game_exist(self):
        """
        Checks if Game exists
        """

        e = await self.request.request(
            url=f'https://games.roblox.com/v1/games/multiget-place-details?placeIds={self._id}', method='get')
        if 'placeId' not in e[0]:
            raise GameNotFound("Invalid Game")
        else:
            return self._id

    async def join_game(self):
        """ Joins a server """
        self.process = subprocess.Popen([

            os.path.join(self.game_path, "RobloxPlayerBeta.exe"),
            "--play"
            f"{self.main_game_path}",
            "-a", "https://auth.roblox.com/v1/authentication-ticket/redeem",
            "-t", await self.get_roblox_auth_ticket(),
            "-j", f"\"https://assetgame.roblox.com/game/PlaceLauncher.ashx?request=RequestGame&placeId={self._id}"
                  f"&isPlayTogetherGame=false\"",
        ])

    async def join_game_server(self, server_id: str):
        """

        Joins a specific server by server ID
        Parameters
        ----------
        server_id : str
            Server Id

        """

        self.process = subprocess.Popen([
            os.path.join(self.game_path, "RobloxPlayerBeta.exe"),
            "--play"
            f"{self.main_game_path}",
            "-a", "https://auth.roblox.com/v1/authentication-ticket/redeem",
            "-t", await self.get_roblox_auth_ticket(),
            "-j",
            f"\"https://assetgame.roblox.com/game/PlaceLauncher.ashx?"
            f"request=RequestGameJob&placeId={self._id}&gameId={server_id}&isPlayTogetherGame=false\"",
        ])

    async def kill_game(self):
        """ Kills the Roblox Players """
        self.process.kill()

    # time to use context manager  || change my mind
