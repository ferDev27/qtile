from os import path
import json
from .path import qtile_path

def load_theme(theme='ferDev27'):
    theme_file = path.join(qtile_path, "themes", f'{theme}.json')

    if not path.isfile(theme_file):
        raise Exception(f'"{theme_file}" does not exist')

    with open(path.join(theme_file)) as f:
        return json.load(f)

# Set color scheme
colors = load_theme("gruvbox")
