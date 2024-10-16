from libqtile import widget
from libqtile import qtile
from .theme import colors
from .path import qtile_path

def custom_spacer(background=colors['darker'], foreground=colors['light'], length=10):
    return widget.Spacer(background=background, foreground=foreground, length=length)

def empty_win_name():
    return widget.WindowName(background=colors['darker'], padding=0, fmt= '')

def right_separator(icon="", size=38, padding=0):
    return {
        'text': icon,
        'fontsize': size,
        'padding': padding
    }

def left_separator(icon="", size=38, padding=0):
    return {
        'text': icon,
        'fontsize': size,
        'padding': padding
    }

custom_icon = "ferDev27.png"

primary_widgets = [
    # Left section
    custom_spacer(colors['grey'], colors['grey']),
    widget.Image(
        filename=f"{qtile_path}/assets/icons/{custom_icon}",
        background=colors['grey'], 
        margin = 3,
        mouse_callbacks = {'Button1': lambda: qtile.spawn(f"sh {qtile_path}/scripts/power_menu"),},
        ),
    widget.TextBox(
        background=colors['dark'],
        foreground=colors['grey'],
        **right_separator()
        ),
    custom_spacer(colors['dark'], colors['dark']),
    widget.Systray(
            background=colors['dark'],
        ),
    widget.TextBox(
        background=colors['darker'],
        foreground=colors['dark'],
        **right_separator()
        ),

    # Mid section
    # Trick to center GroupBox
    empty_win_name(),
    widget.GroupBox(
        background=colors['darker'],
        borderwidth=2,
        active=colors['active'],
        inactive=colors['inactive'],
        highlight_method='line',
        highlight_color=[colors['dark'], colors['dark']],
        this_current_screen_border=colors['focus'],
        this_screen_border=colors['sfocus'],
        other_current_screen_border = colors['nonfocus'],
        other_screen_border = colors['nonfocus']
        ),
    empty_win_name(),

    # Right section
    widget.TextBox(
        background=colors['darker'],
        foreground=colors['dark'],
        **left_separator()
        ),
    widget.TextBox(
        background=colors['dark'],
        foreground=colors['grey'],
        **left_separator()
        ),
    widget.CheckUpdates(
        background=colors['grey'],
        colour_no_updates=colors['widget0'],
        colour_have_updates=colors['widget1'],
        no_update_string='  0',
        display_format='  {updates}',
        update_interval=1800,
        custom_command='checkupdates'
        ),
    custom_spacer(colors['grey'], colors['grey']),
    widget.TextBox(
        background=colors['grey'],
        foreground=colors['widget2'],
        **left_separator()
        ),
    widget.Net(
        background=colors['widget2'],
        foreground=colors['dark'], 
        interface='wlp0s20f3',
        format='↓{down:6.2f}{down_suffix:<2}↑{up:6.2f}{up_suffix:<2}'
        ),
    widget.TextBox(
        background=colors['widget2'],
        foreground=colors['widget3'],
        **left_separator()
        ),
    widget.Battery(
        background=colors['widget3'],
        foreground=colors['dark'],
        charge_char=" ",
        discharge_char="󰁹",
        empty_char="󰅙 ",
        format='{char} {percent:2.0%}'
        ),
    custom_spacer(colors['widget3'], colors['widget3'], 5),
    widget.TextBox(
        background=colors['widget3'],
        foreground=colors['widget4'],
        **left_separator()
        ),
    widget.Clock(
            background=colors['widget4'],
            foreground=colors['dark'], 
            fmt='󰃰  {}', 
            format='%d-%m-%y | %H:%M '
            ),
    widget.TextBox(
        background=colors['widget4'],
        foreground=colors['darker'],
        **left_separator()
        ),
    widget.CurrentLayoutIcon(
        background=colors['darker'],
        scale=0.60,
        padding=6
        )
]

secondary_widgets = [
    # Left section
    custom_spacer(colors['grey'], colors['grey']),
    widget.Image(
        filename=f"{qtile_path}/assets/icons/{custom_icon}",
        background=colors['grey'], 
        margin = 3,
        mouse_callbacks = {'Button1': lambda: qtile.spawn(f"sh {qtile_path}/scripts/power_menu"),},
        ),
    widget.TextBox(
        background=colors['dark'],
        foreground=colors['grey'],
        **right_separator()
        ),
    widget.TextBox(
        background=colors['darker'],
        foreground=colors['dark'],
        **right_separator()
        ),

    # Mid section
    # Trick to center GroupBox
    empty_win_name(),
    widget.GroupBox(
        background=colors['darker'],
        borderwidth=2,
        active=colors['active'],
        inactive=colors['inactive'],
        highlight_method='line',
        highlight_color=[colors['dark'], colors['dark']],
        this_current_screen_border=colors['focus'],
        this_screen_border=colors['sfocus'],
        other_current_screen_border = colors['nonfocus'],
        other_screen_border = colors['nonfocus']
        ),
    empty_win_name(),

    # Right section
    widget.TextBox(
        background=colors['darker'],
        foreground=colors['dark'],
        **left_separator()
        ),
    widget.TextBox(
        background=colors['dark'],
        foreground=colors['grey'],
        **left_separator()
        ),
    widget.TextBox(
        background=colors['grey'],
        foreground=colors['light'],
        text="  Qtile "
        ),
    widget.TextBox(
        background=colors['grey'],
        foreground=colors['widget4'],
        **left_separator()
        ),
    widget.Clock(
            background=colors['widget4'],
            foreground=colors['dark'], 
            fmt='󰃰  {}', 
            format='%d-%m-%y | %H:%M '
            ),
    widget.TextBox(
        background=colors['widget4'],
        foreground=colors['darker'],
        **left_separator()
        ),
    widget.CurrentLayoutIcon(
        background=colors['darker'],
        scale=0.60,
        padding=6
        )
]

widget_defaults = dict(
    font="Ubuntu Mono Nerd Font Bold",
    fontsize=19,
    padding=3,
)
extension_defaults = widget_defaults.copy()

