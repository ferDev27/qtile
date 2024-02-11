from libqtile.config import Key
from libqtile.command import lazy
from .software import terminal, browser
from .path import qtile_path

# Leader key
mod = "mod4"

keys = [
    # Qtile keys ---------------------------------------------------------------

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), 
        desc="Move focus to left"),

    Key([mod], "l", lazy.layout.right(), 
        desc="Move focus to right"),

    Key([mod], "j", lazy.layout.down(), 
        desc="Move focus down"),

    Key([mod], "k", lazy.layout.up(), 
        desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), 
        desc="Move window to the left"),

    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), 
        desc="Move window to the right"),

    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), 
        desc="Move window down"),

    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), 
        desc="Move window up"),

    # Grow/Shrink windows
    Key([mod, "control"], "l", lazy.layout.grow(), 
        desc="Grow window up"),

    Key([mod, "control"], "h", lazy.layout.shrink(), 
        desc="Shrink window down"),

    # Reset window sizes
    Key([mod], "n", lazy.layout.reset(), 
        desc="Reset all window sizes"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), 
        desc="Toggle up between layouts"),

    Key([mod, "shift"], "Tab", lazy.prev_layout(), 
        desc="Toggle down between layouts"),

    # Toggle full screen
    Key(
        [mod], "f", lazy.window.toggle_fullscreen(), 
        desc="Toggle fullscreen on a window",),

    # Toggle floating
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), 
        desc="Toggle floating on a focused window"),

    # Kill window
    Key([mod], "w", lazy.window.kill(), 
        desc="Kill focused window"),

    # Move between monitors
    Key([mod], "period", lazy.next_screen(), 
        desc="Switch focus to next screen"),

    Key([mod], "comma", lazy.prev_screen(), 
        desc="Switch focus to prev screen"),

    # Reload and quit Qtile
    Key([mod, "control"], "r", lazy.reload_config(), 
        desc="Reload the config"),

    Key([mod, "control"], "q", lazy.shutdown(), 
        desc="Shutdown Qtile"),

    # Software Keys ------------------------------------------------------------

    # Terminal
    Key([mod], "Return", lazy.spawn(terminal), 
        desc="Launch terminal"),

    # Menu
    Key([mod], "space", lazy.spawn("rofi -show run"), 
        desc="Launch rofi menu"),

    Key([mod, "shift"], "space", lazy.spawn("rofi -show"), 
        desc="Launch rofi window selector"),

    # Screenshots
    Key([mod], "s", lazy.spawn(f"{qtile_path}/scripts/screenshot"), 
        desc="Take a full screen screenshot"),
    Key([mod, "shift"], "s", lazy.spawn(f"{qtile_path}/scripts/screenshot-s"), 
        desc="Select area and take a screenshot"),

    # Color picker
    Key([mod], "p", lazy.spawn(f"{qtile_path}/scripts/picker"), 
        desc="Launch color picker"),

    # Browser
    Key([mod], "b", lazy.spawn("firefox"), 
        desc="Launch browser"),
    
    # Redshift
    Key([mod], "r", lazy.spawn("redshift -O 3600"), 
        desc="Turn eyecare on"),
    Key([mod, "shift"], "r", lazy.spawn("redshift -x"), 
        desc="Turn eyecare off"),

    # System Keys --------------------------------------------------------------

    # Volume 
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )
