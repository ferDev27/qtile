from libqtile import widget
from .theme import colors
from .path import qtile_path


def gap(padding=5):
    return {
        'linewidth': 0,
        'padding': padding
    }

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

primary_widgets = [
                widget.CurrentLayoutIcon(
                    background=colors['darker'],
                    scale=0.65,
                    padding=15
                    ),
                widget.CurrentLayout(
                    background=colors['darker'],
                    foreground=colors['light'],
                    ),
                widget.TextBox(
                    background=colors['dark'],
                    foreground=colors['darker'],
                    **right_separator()
                    ),
                widget.TextBox(
                    background=colors['darker'],
                    foreground=colors['dark'],
                    **right_separator()
                    ),
                widget.Sep(
                    background=colors['darker'],
                    foreground=colors['darker'],
                    ),
                widget.WindowName(
                    foreground=colors['widget4'], 
                    background=colors['darker'], 
                    fontsize=18, 
                    padding=15,
                    #max_chars=67
                    fmt= ''
                    ),
                widget.GroupBox(
                    background=colors['darker'],
                    borderwidth=2,
                    active=colors['active'],
                    inactive=colors['inactive'],
                    highlight_method='line',
                    highlight_color=[colors['darker'], colors['dark']],
                    this_current_screen_border=colors['focus'],
                    this_screen_border=colors['grey']
                    ),
                widget.Sep(
                    background=colors['darker'],
                    foreground=colors['darker'],
                    ),
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
                widget.Sep(
                    background=colors['grey'],
                    foreground=colors['grey'],
                    **gap()
                    ),
                widget.TextBox(
                    background=colors['grey'],
                    foreground=colors['widget2'],
                    **left_separator()
                    ),
                widget.Net(
                    background=colors['widget2'],
                    foreground=colors['dark'], 
                    interface='wlp3s0',
                    format='↓{down:6.2f}{down_suffix:<2}↑{up:6.2f}{up_suffix:<2}'
                    ),
                widget.TextBox(
                    background=colors['widget2'],
                    foreground=colors['widget3'],
                    **left_separator()
                    ),
                widget.TextBox(
                    background=colors['widget3'],
                    foreground=colors['dark'],
                    text="  Qtile "
                    ),
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
                widget.Systray(
                        background=colors['darker'],
                    )
            ]

widget_defaults = dict(
    font="Ubuntu Mono Nerd Font Bold",
    fontsize=19,
    padding=3,
)
extension_defaults = widget_defaults.copy()

