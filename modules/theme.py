from os import path
import json
from .path import qtile_path
import subprocess

# Available themes are ferDev27, catppuccin, synthwave, gruvbox, aura
theme = "aura"

# Load theme json data
def load_theme():
    theme_file = path.join(qtile_path, "themes", f'{theme}.json')

    if not path.isfile(theme_file):
        raise Exception(f'"{theme_file}" does not exist')

    with open(path.join(theme_file)) as f:
        return json.load(f)


# Set Wallpaper
wallpaper_name = f"{theme}.jpg"
def set_wallpaper():
    subprocess.call(f"feh --bg-fill {qtile_path}/assets/wallpapers/{wallpaper_name} &", shell=True)

# Set theme
colors = load_theme()
set_wallpaper()
