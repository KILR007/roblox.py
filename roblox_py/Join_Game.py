import json
import os
import time
import getpass
from .exceptions import *
import subprocess

class JoinGame:
    """
    Represents a Game Join class.

    """
    def __init__(self,request,Game_ID,roblox_game_path=None,roblox_folder_path=None):
        if roblox_folder_path is None:
            self.main_game_path = f'C:/Users/{getpass.getuser()}/AppData/Local/Roblox'
        else:
            self.main_game_path = roblox_folder_path

        self._id = Game_ID
        self.request = request
        self.robloxLocalStoragePath = f'{self.main_game_path}/LocalStorage'
        self.brower_track_id_path = f'{self.robloxLocalStoragePath}/appStorage.json'
        self.version_path = f'{self.main_game_path}/Versions'
        self.brower_track_id = None
        with open(self.brower_track_id_path, "r") as f:
            data = json.load(f)
            browserTrackerId = data['BrowserTrackerId']
        self.browserTrackerId = browserTrackerId
        self.game_path = None
        templates = [

            "C:/Program Files (x86)/Roblox/Versions",
            "C:/Program Files/Roblox/Versions",
            f"C:/Users/{getpass.getuser()}/AppData/Local/Roblox/Versions",
        ]
        if roblox_game_path is None:
            for a in templates:
                for root, dirs, files in os.walk(a):
                    for names in files:
                        if names.startswith("RobloxPlayerBeta"):
                            self.game_path = f"{root}"
        else:
            self.game_path = f"{roblox_game_path}"







    async def _rblx_token(self):
        e = await self.request.return_headers(url='https://auth.roblox.com/v1/authentication-ticket/',method='post')
        return str(e['rbx-authentication-ticket'])
    async def get_game_info(self):
        e  = await self.request.request(url=f'https://games.roblox.com/v1/games/multiget-place-details?placeIds={self._id}',method='get')
        if 'placeId' not in e[0]:
            raise GameNotFound("Invalid Game")
        else:
            return self._id

    async def join_game(self):
        self.process = subprocess.Popen([
            os.path.join(self.game_path, "RobloxPlayerBeta.exe"),
            f"{self.main_game_path}",
            "-id ", str(await self.get_game_info()),
            "-a", '\"https://www.roblox.com\"',
            "-t", await self._rblx_token(),
            "-j", f"\"https://assetgame.roblox.com/game/PlaceLauncher.ashx?request=RequestGame&browserTrackerId={self.browserTrackerId}&placeId={self._id}&isPlayTogetherGame=false\"",
            '-b', str(self.browserTrackerId),
            f"--launchtime={int(time.time() * 1000)}",
            "--rloc", "en_us",
            "--gloc", "en_us"
        ])
    async def join_game_server(self,server_id):
        self.process = subprocess.Popen([
            os.path.join(self.game_path, "RobloxPlayerBeta.exe"),
            f"{self.main_game_path}",
            "-id ",str(await self.get_game_info()),
            "-a", '\"https://www.roblox.com/Login/Negotiate.ashx\"',
            "-t", await self._rblx_token(),
            "-j",
            f"\"https://assetgame.roblox.com/game/PlaceLauncher.ashx?request=RequestGameJob&browserTrackerId={self.browserTrackerId}&placeId={self._id}&gameId={server_id}&isPlayTogetherGame=false\"",
            '-b', str(self.browserTrackerId),
            f"--launchtime={int(time.time() * 1000)}",
            "--rloc", "en_us",
            "--gloc", "en_us"
        ])
    async def kill_game(self):
        self.process.kill()


    # time to use context manager  || change my mind

