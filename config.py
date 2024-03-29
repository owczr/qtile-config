# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import subprocess

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


mod = "mod4"
alt = "mod1"
terminal = guess_terminal()


GAP_SIZE = 4
BORDER_SIZE = 2
WALLPAPER = "~/.config/qtile/wallpaper.png"
ICONS_DIR = "~/Pictures/icons/"
SCRIPTS_DIR = "~/.config/qtile/scripts"


@hook.subscribe.startup
def run_on_startup():
    script = os.path.expanduser(os.path.join(SCRIPTS_DIR, "autostart.sh"))
    subprocess.call([script])

def open_chromium():
    return lazy.spawn("chromium")

def open_rofi():
    return lazy.spawn("rofi -show drun -show-icons")

def open_rofimoji():
    return lazy.spawn("rofimoji -a clipboard")

def open_terminal():
    return lazy.spawn("alacritty")

def open_thunderbird():
    return lazy.spawn("thunderbird")

def open_vscode():
    return lazy.spawn("codium")

def open_discord():
    return lazy.spawn("discord")

def open_nemo():
    return lazy.spawn("nemo")

def open_spotify():
    return lazy.spawn("spotify-launcher")

def open_todoist():
    return lazy.spawn("todoist")

def open_obsidian():
    return lazy.spawn("obsidian")

def turn_off_laptop_screen():
    script = os.path.expanduser(os.path.join(SCRIPTS_DIR, "turn_off_laptop_screen.sh"))
    subprocess.call([script])

BACKGROUND = "#1e1e2e"
FOREGROUND_LIGHT = "#cdd6f4"
FOREGROUND_DARK = "#11111b"
GRAY = "#313244"
MAUVE = "#cba6f7"
RED = "#f38ba8"
YELLOW = "#f9e2af"
GREEN = "#a6e3a1"
BLUE = "#89b4fa"
ROSEWATER = "#f5e0dc"
FLAMINGO = "#f2cdcd"
PINK = "#f5c2e7"
SKY = "#89dceb"
PEACH = "#fab387"
ACCENT = BLUE

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key(["control", alt], "t", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "space", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([alt], "space", open_rofi(), desc="Spawn Rofi"),
    Key([mod], "period", open_rofimoji(), desc="Spawn emoji picker")
]

groups = [
    Group(name=name, label=label)
    for name, label 
    in zip("123456789", ["󰮯", "", "", "", "", "󰊠","󰊠", "󰊠", "󰊠"])
]
for g in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                g.name,
                lazy.group[g.name].toscreen(),
                desc="Switch to group {}".format(g.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                g.name,
                lazy.window.togroup(g.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(g.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus_stack=[GRAY, GRAY],
        border_focus=ACCENT,
        border_width=BORDER_SIZE,
        margin=GAP_SIZE
    ),
    layout.Max(
        margin=GAP_SIZE,
    ),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="NotoSans Nerd Font",
    fontsize=16,
    padding=5,
    margin=2,
    foreground=FOREGROUND_LIGHT,
)
extension_defaults = widget_defaults.copy()

IMAGE_PADDING = 5

def create_group_boxes():
    return [
        widget.GroupBox(
            highlight_method="text",
            this_current_screen_border=YELLOW,
            this_screen_border=YELLOW,
            other_current_screen_border=GRAY,
            other_screen_border=GRAY,
            disable_drag=True,
            foreground=FOREGROUND_LIGHT,
            active=FOREGROUND_LIGHT,
            inactive=GRAY,
            visible_groups=["1"],
        ),
        widget.GroupBox(
            highlight_method="text",
            this_current_screen_border=ROSEWATER,
            this_screen_border=ROSEWATER,
            other_current_screen_border=GRAY,
            other_screen_border=GRAY,
            disable_drag=True,
            foreground=FOREGROUND_LIGHT,
            active=FOREGROUND_LIGHT,
            inactive=GRAY,
            visible_groups=["2", "3", "4", "5"],
        ),
        widget.GroupBox(
            highlight_method="text",
            this_current_screen_border=RED,
            this_screen_border=RED,
            other_current_screen_border=GRAY,
            other_screen_border=GRAY,
            disable_drag=True,
            foreground=FOREGROUND_LIGHT,
            active=FOREGROUND_LIGHT,
            inactive=GRAY,
            visible_groups=["6"],
        ),
        widget.GroupBox(
            highlight_method="text",
            this_current_screen_border=PEACH,
            this_screen_border=PEACH,
            other_current_screen_border=GRAY,
            other_screen_border=GRAY,
            disable_drag=True,
            foreground=FOREGROUND_LIGHT,
            active=FOREGROUND_LIGHT,
            inactive=GRAY,
            visible_groups=["7"],
        ),
        widget.GroupBox(
            highlight_method="text",
            this_current_screen_border=SKY,
            this_screen_border=SKY,
            other_current_screen_border=GRAY,
            other_screen_border=GRAY,
            disable_drag=True,
            foreground=FOREGROUND_LIGHT,
            active=FOREGROUND_LIGHT,
            inactive=GRAY,
            visible_groups=["8"],
        ),
        widget.GroupBox(
            highlight_method="text",
            this_current_screen_border=PINK,
            this_screen_border=PINK,
            other_current_screen_border=GRAY,
            other_screen_border=GRAY,
            disable_drag=True,
            foreground=FOREGROUND_LIGHT,
            active=FOREGROUND_LIGHT,
            inactive=GRAY,
            visible_groups=["9"],
        ),
    ]

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                ),
                widget.TextBox(
                    "󰣇",
                    mouse_callbacks={"Button1": open_rofi()},
                    foreground=ROSEWATER,
                    fontsize=24,
                    margin=0,
                ),
                *create_group_boxes(),
                widget.StatusNotifier(
                ),
                widget.Prompt(),
                widget.WindowName(
                    format="{name} {state}",
                ),
                widget.Notify(
                    audiofile="~/Music/notification.mp3",
                    background=BACKGROUND,
                    background_low=BACKGROUND,
                    background_urgent=BACKGROUND,
                ),
                widget.Sep(
                    linewidth=0,
                ),
                widget.WidgetBox(
                    text_closed="",
                    text_open="",
                    close_button_location="right",
                    foreground=FLAMINGO,
                    widgets=[
                        widget.TextBox(
                            "",
                            foreground=FLAMINGO,
                        ),
                        widget.Sep(
                            linewidth=0,
                            foreground=FLAMINGO,
                        ),
                        widget.Net(
                            format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
                            foreground=FLAMINGO,
                        ),
                        widget.TextBox(
                            "",
                            foreground=FLAMINGO,
                        ),
                        widget.CPU(
                            format=" {load_percent}%",
                            foreground=FLAMINGO,
                        ),
                        widget.Sep(
                            linewidth=0,
                            foreground=FLAMINGO,
                        ),
                        widget.TextBox(
                            "",
                            foreground=FLAMINGO,
                        ),
                        widget.Memory(
                            format=" {MemPercent}%",
                            foreground=FLAMINGO,
                        ),
                        widget.Sep(
                            linewidth=0,
                            foreground=FLAMINGO,
                        ),

                        widget.TextBox(
                            "󰖙",
                            foreground=FLAMINGO,
                        ),
                        widget.OpenWeather(
                            location="Kraków",
                            format=" {temp}°C",
                            foreground=FLAMINGO,
                        ),
                    ]
                ),
                widget.WidgetBox(
                    foreground=ROSEWATER,
                    text_closed="",
                    text_open="",
                    close_button_location="right",
                    widgets=[
                        widget.TextBox(
                            "󰕾",
                            foreground=ROSEWATER,
                        ),
                        widget.Volume(
                            fmt="{}",
                            foreground=ROSEWATER,
                        ),
                        widget.Sep(
                            linewidth=0,
                            foreground=ROSEWATER,
                        ),
                        widget.TextBox(
                            "󰌌",
                            foreground=ROSEWATER,
                        ),
                        widget.KeyboardLayout(
                            configured_keyboards=["us", "pl"],
                            foreground=ROSEWATER,
                        ),
                        widget.Sep(
                            linewidth=0,
                            foreground=ROSEWATER,
                        ),
                        widget.TextBox(
                            "",
                            foreground=ROSEWATER,
                        ),
                        widget.CurrentLayout(
                            foreground=ROSEWATER,
                        ),
                        widget.Sep(
                            linewidth=0,
                            foreground=ROSEWATER,
                        ),
                    ],
                ),
                widget.TextBox(
                    "󰃭",
                    foreground=MAUVE,
                ),
                widget.Clock(
                    format="%Y-%m-%d",
                    foreground=MAUVE,
                ),
                widget.TextBox(
                    "󰥔",
                    foreground=GREEN,
                ),
                widget.Clock(
                    format="%H:%M",
                    foreground=GREEN,
                ),
                widget.TextBox(
                    "󰁹",
                    foreground=YELLOW,
                ),
                widget.Battery(
                    format="{char} {percent:2.0%}",
                    notify_below=10.0,
                    charge_char="󰶣",
                    discharge_char="󰶡",
                    empty_char="󰚌",
                    full_char="󱐋",
                    foreground=YELLOW,
                ),
                widget.TextBox(
                    "󰐥",
                    foreground=RED,
                    margin=3,
                ),
                widget.QuickExit(
                    default_text="Exit",
                    countdown_format="{} s",
                    foreground=RED,
                ),
                widget.Sep(
                    linewidth=0,
                ),
            ],
            32,
            background=BACKGROUND,
            opacity=0.9,
            margin=[
                GAP_SIZE * 2,
                GAP_SIZE * 2,
                GAP_SIZE,
                GAP_SIZE * 2,
            ],
        ), 
        wallpaper=WALLPAPER,
        wallpaper_mode="stretch",
        left=bar.Gap(size=GAP_SIZE),
        right=bar.Gap(size=GAP_SIZE),
        bottom=bar.Gap(size=GAP_SIZE),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                ),
                widget.TextBox(
                    "󰣇",
                    mouse_callbacks={"Button1": open_rofi()},
                    foreground=ROSEWATER,
                    fontsize=24,
                    margin=0,
                ),
                *create_group_boxes(),
                widget.WindowName(
                    background=BACKGROUND,
                ),
                widget.Spacer(
                    bar.STRETCH,
                ),
                widget.TextBox(
                    "󰥔",
                    foreground=GREEN,
                ),
                widget.Clock(
                    format="%H:%M",
                    foreground=GREEN,
                ),
                widget.TextBox(
                    "󰁹",
                    foreground=YELLOW,
                ),
                widget.Battery(
                    format="{char} {percent:2.0%}",
                    notify_below=10.0,
                    charge_char="󰶣",
                    discharge_char="󰶡",
                    empty_char="󰚌",
                    full_char="󱐋",
                    foreground=YELLOW,
                ),
                widget.TextBox(
                    "󰍹  Off",
                    foreground=RED,
                    mouse_callbacks={"Button1": turn_off_laptop_screen},
                ),
                widget.Sep(
                    linewidth=0,
                ),
            ],
            32,
            background=BACKGROUND,
            opacity=0.9,
            margin=[
                GAP_SIZE * 2,
                GAP_SIZE * 2,
                GAP_SIZE,
                GAP_SIZE * 2,
            ],
        ), 
        wallpaper=WALLPAPER,
        wallpaper_mode="stretch",
        left=bar.Gap(size=GAP_SIZE),
        right=bar.Gap(size=GAP_SIZE),
        bottom=bar.Gap(size=GAP_SIZE),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=ACCENT,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
)
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
