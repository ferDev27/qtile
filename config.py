#
#              __           ____             ____ _____
#             / _| ___ _ __|  _ \  _____   _|___ \___  |
#            | |_ / _ \ '__| | | |/ _ \ \ / / __) | / /
#            |  _|  __/ |  | |_| |  __/\ V / / __/ / /
#            |_|  \___|_|  |____/ \___| \_/ |_____/_/
#
#              GitHub: https://github.com/ferDev27
#

# Qtile libraries
from libqtile import hook

# Python libraries
from os import path
import subprocess

# Configuration modules
from modules.path import qtile_path
from modules.software import terminal, browser
from modules.keybinds import mod, keys
from modules.mouse import mouse
from modules.groups import groups
from modules.layouts import layouts, floating_layout
from modules.widgets import widget_defaults, extension_defaults
from modules.screens import screens


# Auto start script
@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'scripts', 'autostart.sh')])

# Set Wallpaper
@hook.subscribe.startup_once
def set_wallpaper():
    subprocess.call(f"feh --bg-fill {qtile_path}/wallpapers/space.png &", shell=True)

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False


auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
