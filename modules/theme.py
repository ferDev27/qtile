from os import path
import json
from .path import qtile_path
import subprocess

# Load theme json data
def json_color_scheme(theme_name):
    theme_file = path.join(qtile_path, "themes", f'{theme_name}.json')

    if not path.isfile(theme_file):
        raise Exception(f'"{theme_file}" does not exist')

    with open(path.join(theme_file)) as f:
        return json.load(f)

# Set Wallpaper
def set_wallpaper(wallpaper_name):
    subprocess.call(f"feh --bg-fill {qtile_path}/assets/wallpapers/{wallpaper_name} &", shell=True)
