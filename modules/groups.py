from libqtile.config import Key, Group
from libqtile.command import lazy
from .keybinds import mod, keys

workspaces = [" 󰇧  ", "   ", "   ", " 󰊢  ", "   ", "   ", " 󰋩  ", "   ", " 󰘸  "]
groups = [Group(ws) for ws in workspaces]

for i, group in enumerate(groups):
    index = str(i + 1)
    keys.extend(
        [
            # mod1 + index = switch to group
            Key(
                [mod],
                index,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + index = switch to & move focused window to group
            #Key(
            #    [mod, "shift"],
            #    index,
            #    lazy.window.togroup(group.name, switch_group=True),
            #    desc="Switch to & move focused window to group {}".format(group.name),
            #),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + index = move focused window to group
            Key([mod, "shift"], index, lazy.window.togroup(group.name),
                desc="move focused window to group {}".format(group.name)),
        ]
    )

