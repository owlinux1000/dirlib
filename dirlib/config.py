import os
import sys
from pathlib import Path

def user_config_dir(platform:str = sys.platform):
    dir = ""
    match platform:
        case "win32":
            dir = os.getenv("AppData")
            if dir is None:
                dir = os.getenv("UserProfile")
                if dir is None:
                    raise 'neither %AppData% nor %UserProfile% are defined'
            return dir

        case "darwin":
            dir = os.getenv("HOME")
            if dir is None:
                raise '$HOME is not defined'
            path = Path(dir)
            path.joinpath("/Libary/Application Support")
            return str(path)

        case "linux":
            dir = os.getenv("XDG_CONFIG_HOME")
            if dir is None:
                dir = os.getenv("HOME")
                if dir is None:
                    raise 'neither $XDG_CONFIG_HOME nor $HOME are defined'
            path = Path(dir)
            path.joinpath("./config")
            return str(path)

        case _:
            raise "Your platform is not supproted. Currently, dirlib supports Windows, Unix and macOS"