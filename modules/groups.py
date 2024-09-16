from libqtile.config import Key, Group, ScratchPad, DropDown
from libqtile.lazy import lazy
from .keybinds import mod, keys
from .software import terminal

workspaces = ["   ", "   ", " 󰨞  ", "   ", " 󰘸  ", "   "]
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
# Scratchpads
groups.append(ScratchPad('scratchpad', [
    DropDown('terminal', str(terminal), width=0.8, height=0.8, x=0.1, y=0.1)
    ]))
