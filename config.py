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


GAP_SIZE = 8
BORDER_SIZE = 2
WALLPAPER = "~/.config/qtile/wallpaper.jpg"
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

def open_wifi_menu():
    script = os.path.expanduser(os.path.join(SCRIPTS_DIR, "rofi-wifi-menu.sh"))
    return lambda : subprocess.call([script])

COLORS = [
    "#04060c",
    "#4a586f",
    "#536179",
    "#923b4a",
    "#596986",
    "#5c6388",
    "#687691",
    "#b3bac7",
    "#7d828b",
    "#4a586f",
    "#536179",
    "#923b4a",
    "#596986",
    "#5c6388",
    "#687691",
    "#b3bac7",
]

DARK_RED_COLORS = [   
    "#6d2c37",
    "#481e25",
    "#240f13",
]

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
    Key([mod], "space", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([alt], "space", open_rofi(), desc="Spawn Rofi"),
    Key([mod], "period", open_rofimoji(), desc="Spawn emoji picker")
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus_stack=[COLORS[1], COLORS[2]],
        border_focus=COLORS[3],
        border_width=BORDER_SIZE,
        margin=GAP_SIZE
    ),
    layout.Max(),
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
    font="Noto Sans",
    fontsize=14,
    padding=4,
    margin=2,
)
extension_defaults = widget_defaults.copy()

IMAGE_PADDING = 5

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                    filename=os.path.join(ICONS_DIR, "arch-logo-white.png"),
                    mouse_callbacks={"Button1": open_rofi()},
                    margin=1,
                ),
                widget.GroupBox(
                    highlight_method="line",
                    this_current_screen_border=COLORS[3],
                    this_screen_border=COLORS[3],
                    other_current_screen_border=COLORS[8],
                    other_screen_border=COLORS[8],
                    disable_drag=True,
                ),
                widget.WidgetBox(
                    text_closed="apps",
                    text_open="[apps]",
                    background=COLORS[3],
                    widgets=[
                        widget.Image(
                            filename=os.path.join(ICONS_DIR, "chrome.svg"),
                            mouse_callbacks={"Button1": open_chromium()},
                            margin=1,
                            background=COLORS[0],
                        ),
                        widget.Sep(
                            linewidth=0,
                            padding=IMAGE_PADDING,
                            background=COLORS[0],
                        ),
                        widget.Image(
                            filename=os.path.join(ICONS_DIR, "thunderbird.svg"),
                            mouse_callbacks={"Button1": open_thunderbird()},
                            margin=3,
                            background=COLORS[0],
                        ),
                        widget.Sep(
                            linewidth=0,
                            padding=IMAGE_PADDING,
                            background=COLORS[0],
                        ),
                        widget.Image(
                            filename=os.path.join(ICONS_DIR, "terminal.svg"),
                            mouse_callbacks={"Button1": open_terminal()},
                            margin=0,
                            background=COLORS[0],
                        ),
                        widget.Sep(
                            linewidth=0,
                            padding=IMAGE_PADDING,
                            background=COLORS[0],
                        ),
                        widget.Image(
                            filename=os.path.join(ICONS_DIR, "folder.svg"),
                            mouse_callbacks={"Button1": open_nemo()},
                            margin=3,
                            background=COLORS[0],
                        ),
                        widget.Sep(
                            linewidth=0,
                            padding=IMAGE_PADDING,
                            background=COLORS[0],
                        ),
                        widget.Image(
                            filename=os.path.join(ICONS_DIR, "vscode.svg"),
                            mouse_callbacks={"Button1": open_vscode()},
                            background=COLORS[0],
                        ),
                        widget.Sep(
                            linewidth=0,
                            padding=IMAGE_PADDING,
                            background=COLORS[0],
                        ),
                        widget.Image(
                            filename=os.path.join(ICONS_DIR, "discord.svg"),
                            mouse_callbacks={"Button1": open_discord()},
                            background=COLORS[0],
                        ),
                        widget.Sep(
                            linewidth=0,
                            padding=IMAGE_PADDING,
                            background=COLORS[0],
                        ),
                        widget.Image(
                            filename=os.path.join(ICONS_DIR, "spotify.svg"),
                            mouse_callbacks={"Button1": open_spotify()},
                            margin=3,
                            background=COLORS[0],
                        ),
                        widget.Sep(
                            linewidth=0,
                            padding=IMAGE_PADDING,
                            background=COLORS[0],
                        ),
                        widget.Image(
                            filename=os.path.join(ICONS_DIR, "todoist.svg"),
                            mouse_callbacks={"Button1": open_todoist()},
                            margin=3,
                            background=COLORS[0],
                        ),
                        widget.Sep(
                            linewidth=0,
                            padding=IMAGE_PADDING,
                            background=COLORS[0],
                        ),
                        widget.Image(
                            filename=os.path.join(ICONS_DIR, "obsidian.svg"),
                            mouse_callbacks={"Button1": open_obsidian()},
                            margin=0,
                            background=COLORS[0],
                        ),
                        widget.Sep(
                            linewidth=0,
                            padding=IMAGE_PADDING,
                            background=COLORS[0],
                        ),
                    ],
                ),
                widget.Prompt(),
                widget.WindowName(),

                widget.Sep(
                    linewidth=0,
                ),
                widget.Image(
                    filename=os.path.join(ICONS_DIR, "cpu.svg"),
                ),
                widget.CPU(
                    format=" {load_percent}%"
                ),
                widget.Sep(
                    linewidth=0,
                ),
                widget.Image(
                    filename=os.path.join(ICONS_DIR, "ram.svg"),
                ),
                widget.Memory(
                    format=" {MemPercent}%"
                ),
                widget.Sep(
                    linewidth=0,
                ),
                widget.Image(
                   filename=os.path.join(ICONS_DIR, "battery.svg"),
                ),
                widget.Battery(
                    format=" {percent:2.0%}"
                ),
                widget.Sep(
                    linewidth=0,
                ),
                widget.Image(
                    filename=os.path.join(ICONS_DIR, "weather.svg"),
                ),
                widget.OpenWeather(
                    location="Kraków",
                    format=" {temp}°C"
                ),

                widget.Image(
                    filename=os.path.join(ICONS_DIR, "wifi.svg"),
                    mouse_callbacks={"Button1": open_wifi_menu()},
                    background=DARK_RED_COLORS[2],
                ),
                widget.Sep(
                    linewidth=0,
                    background=DARK_RED_COLORS[2],
                ),
                widget.Net(
                    format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
                    background=DARK_RED_COLORS[2],
                    mouse_callbacks={"Button1": open_wifi_menu()},
                ),
                widget.Image(
                    filename=os.path.join(ICONS_DIR, "volume.svg"),
                    background=DARK_RED_COLORS[2],
                ),
                widget.Volume(
                    fmt="{}",
                    background=DARK_RED_COLORS[2],
                ),
                widget.Sep(
                    linewidth=0,
                    background=DARK_RED_COLORS[2],
                ),
                widget.Image(
                    filename=os.path.join(ICONS_DIR, "keyboard.svg"),
                    background=DARK_RED_COLORS[2],
                ),
                widget.KeyboardLayout(
                    configured_keyboards=["us", "pl"],
                    background=DARK_RED_COLORS[2],
                ),
                widget.Sep(
                    linewidth=0,
                    background=DARK_RED_COLORS[2],
                ),
                widget.CurrentLayoutIcon(
                    scale=0.7,
                    background=DARK_RED_COLORS[2],
                ),
                widget.CurrentLayout(
                    background=DARK_RED_COLORS[2],
                ),
                widget.Sep(
                    linewidth=0,
                    background=DARK_RED_COLORS[2],
                ),
                widget.Image(
                    filename=os.path.join(ICONS_DIR, "clock.svg"),
                    background=DARK_RED_COLORS[1],
                ),
                widget.Clock(
                    format="%Y-%m-%d %H:%M",
                    background=DARK_RED_COLORS[1],
                ),
                widget.Image(
                    filename=os.path.join(ICONS_DIR, "power.svg"),
                    background=DARK_RED_COLORS[0],
                ),
                widget.QuickExit(
                    default_text="Exit",
                    countdown_format="{} s",
                    background=DARK_RED_COLORS[0],
                ),
            ],
            24,
            background=COLORS[0],
            opacity=0.7,
            margin=[
                GAP_SIZE,
                GAP_SIZE,
                0,
                GAP_SIZE,
            ],
        ), 
        # right=bar.Gap(GAP_SIZE),
        # left=bar.Gap(GAP_SIZE),
        # bottom=bar.Gap(GAP_SIZE),
        wallpaper=WALLPAPER,
        wallpaper_mode="stretch",
    ),
    Screen(
        wallpaper=WALLPAPER,
        wallpaper_mode="stretch",
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
    border_focus=COLORS[3],
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
