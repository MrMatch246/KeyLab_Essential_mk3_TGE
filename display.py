# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_Essential_mk3\display.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 6208 bytes
from __future__ import absolute_import, print_function, unicode_literals
from dataclasses import dataclass
from enum import Enum
from functools import partial
from typing import Optional, Tuple, Union

from ableton.v3.control_surface.display import DefaultNotifications, \
    DisplaySpecification, Text, view
from ableton.v3.live import display_name, is_arrangement_view_active, \
    is_track_armed, liveobj_name, song
from .Settings import *

Line1Text = partial(Text, max_width=11, justification=(Text.Justification.NONE))
Line2Text = partial(Text, max_width=20, justification=(Text.Justification.NONE))


class IconType(Enum):
    NONE = 0
    ARTURIA = 1
    RETURN = 2
    BIG_BASS = 3
    SMALL_BASS = 4
    BIG_BRASS = 5
    SMALL_BRASS = 6
    BLACK_KEYS_MAYBE = 7
    DAW = 8
    CLOCK = 9
    X_ICON = 10
    BIG_DRUMS = 11
    SMALL_DRUMS = 12
    BIG_ELECTRIC_PIANO = 13
    SMALL_ELECTRIC_PIANO = 14
    PROCESSOR = 15
    BIG_KEYS = 24
    SMALL_KEYS = 25
    BIG_LEAD = 26
    SMALL_LEAD = 27
    FILLED_HEART = 28
    EMPTY_HEART = 29
    MIDI = 30
    BIG_ORGAN = 31
    SMALL_ORGAN = 32
    BIG_PAD = 33
    SMALL_PAD = 34
    WHITE_ARROW_LEFT = 35
    WHITE_ARROW_RIGHT = 36
    BLACK_ARROW_LEFT = 37
    BLACK_ARROW_RIGHT = 38
    EDIT_PENCIL = 39
    BIG_GRAND_PIANO = 40
    SMALL_GRAND_PIANO = 41
    SMALL_SQUARE_ARROW_CLOCKWISE = 42
    BIG_CYCLE_ARROW_COUNTER_CLOCK = 43
    CYCLE_ARROW_COUNTER_CLOCK = 44
    BIG_SEQUENCE = 45
    SMALL_SEQUENCE = 46
    BIG_SFX = 47
    SMALL_SFX = 48
    BIG_STRINGS = 49
    SMALL_STRINGS = 50
    TEMPLATE = 51
    BROKEN_1 = 52
    BIG_CUSTOM = 53
    SMALL_CUSTOM = 54
    BIG_VOCAL = 55
    SMALL_VOCAL = 56
    DOWN_ARROW = 57
    UP_ARROW = 58
    LEFT_ARROW = 59
    RIGHT_ARROW = 60
    CHECK_MARK = 61
    MIXER = 63
    MAGNIFYING_GLASS = 64
    BIG_SCALES_BOARD = 65
    ARM = 66
    SESSION_RIGHT = 67
    SESSION_LEFT = 68
    BITWIG = 69
    FL_STUDIO = 70
    LIVE = 71
    REASON = 72
    CUBASE = 73



class IconState(Enum):
    UNFRAMED = 0
    CLOSED = 1
    OPENED = 2
    FRAMED = 3


@dataclass
class Icon:
    type = IconType.NONE
    type: IconType
    state = IconState.UNFRAMED
    state: IconState


Lines = Tuple[(str, str)]
Header = str
Footer = Tuple[(Icon, Icon, Icon, Icon)]
Popup = Union[(str, Lines)]


@dataclass
class Frame:
    header: Header
    footer: Footer


@dataclass
class Content:
    primary = None
    primary: Optional[Lines]
    primary_icon = IconType.NONE
    primary_icon: Optional[IconType]
    frame = None
    frame: Optional[Frame]
    popup = None
    popup: Optional[Popup]
    parameters = (
        None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None)
    parameters: Tuple[(Optional[Lines], ...)]


class Notifications(DefaultNotifications):
    identify = lambda: Content(primary=('Connected', ''),
                               primary_icon=(IconType.LIVE))

    class Transport(DefaultNotifications.Transport):
        tap_tempo = lambda tempo: Content(popup=("Tap Tempo", str(int(tempo))))


def get_first_last_track_name(state):
    first_track = state.mixer_session_ring.tracks[0]
    for track in state.mixer_session_ring.tracks[::-1]:
        if track:
            last_track = track
            break
    first = liveobj_name(first_track).ljust(8)[:7].strip()
    last = liveobj_name(last_track).ljust(8)[:8].strip()
    return (first, last)


def get_first_last_param_name(state):
    first_param = state.elements.continuous_controls[0].parameter_name if \
        state.elements.continuous_controls[0].parameter_name else "No"
    last_param = "Device"
    for param in state.elements.continuous_controls[::-1]:
        if param.parameter_name:
            last_param = param.parameter_name
            break
    first = first_param.ljust(8)[:7].strip()
    last = last_param.ljust(8)[:8].strip()
    return (first, last)


def get_device_name(state):
    name = state.device.device.name if state.device.device else "No Device"
    name = name.ljust(13)[:12].strip()
    return f"{name} {state.device_bank_navigation.bank_index + 1}"


def create_root_view() -> view.View[Optional[Content]]:
    @view.View
    def main_view(state) -> Optional[Content]:
        if (state.continuous_control_modes.previous_mode is None) and not (
            state.device_bank_navigation.has_changed_bank_index):
            popup = None
        else:
            if state.continuous_control_modes.selected_mode == "device" and \
                state.device_bank_navigation.has_changed_bank_index:
                (first, last) = get_first_last_param_name(state)
                popup = (get_device_name(state), f"{first} - {last}")
            else:
                (first, last) = get_first_last_track_name(state)
                popup = (
                    f"Tracks {state.mixer_session_ring.offset[0] // ENCODER_TRACK_BANK_TRACKS_PER_CLICK + 1}",
                    f"{first} - {last}")
        if state.elements.tap_button.is_pressed:
            (first, last) = get_first_last_track_name(state)
            popup = (
                f"Tracks {state.mixer_session_ring.offset[0] // ENCODER_TRACK_BANK_TRACKS_PER_CLICK + 1}",
                f"{first} - {last}")





        if state.continuous_control_modes.selected_mode == "mixer":
            icon_1 = Icon(IconType.MIXER,IconState.OPENED)
        else:
            icon_1 = Icon(IconType.MIXER, IconState.CLOSED)

        if is_track_armed(state.target_track.target_track):
            icon_2 = Icon(IconType.ARM, IconState.FRAMED)
        else:
            icon_2 = Icon(IconType.ARM, IconState.UNFRAMED)
        if SCENE_TRACK_NAVIGATION_SWITCH:
            icon_3 = Icon(view_based_content(IconType.UP_ARROW, IconType.UP_ARROW))
        else:
            icon_3 = Icon(view_based_content(IconType.LEFT_ARROW, IconType.UP_ARROW))

        if SCENE_TRACK_NAVIGATION_SWITCH:
            icon_4 = Icon(view_based_content(IconType.DOWN_ARROW, IconType.DOWN_ARROW))
        else:
            icon_4 = Icon(view_based_content(IconType.RIGHT_ARROW, IconType.DOWN_ARROW))

        return Content(primary=(liveobj_name(state.target_track.target_track),
                                display_name(song().view.selected_scene)),
                       parameters=(tuple(((element.parameter_name,
                                           element.parameter_value) if element.parameter_name else None
                                          for element in
                                          state.elements.continuous_controls + [
                                              state.elements.encoder_9,
                                              state.elements.fader_9]))),
                       frame=Frame(header=(
                           view_based_content("Session", "Arrangement")),
                           footer=(icon_1, icon_2, icon_3, icon_4)),
                       popup=popup)

    return view.CompoundView(view.DisconnectedView(),
                             view.NotificationView(lambda _, content: content),
                             main_view)


def view_based_content(session_content, arrangement_content):
    if is_arrangement_view_active():
        return arrangement_content
    return session_content


def protocol(elements):
    def display(content):
        if content:
            display_primary_content(content.primary, content.primary_icon)
            display_frame(content.frame)
            display_popup(content.popup)
            display_parameters(content.parameters)

    def display_primary_content(text, icon):
        if text:
            with elements.display_full_screen_command.deferring_send():
                elements.display_line_1.display_message(text[0])
                elements.display_line_2.display_message(text[1])
                elements.display_full_screen_command.send_value(
                    screen_id=(26 if icon.value else 18), line3=(icon.value))

    def display_frame(frame):
        if frame:
            elements.display_header_command.send_value(
                Text(frame.header).as_ascii())
            (elements.display_footer_command.send_value)(*frame.footer)

    def display_popup(popup):
        if popup:
            (line1, line2) = (popup, None) if isinstance(popup, str) else popup
            elements.display_popup_command.send_value(
                line1=(Text(line1).as_ascii()),
                line2=(Text(line2).as_ascii() if line2 else None))

    def display_parameters(parameters):
        for (command, parameter) in list(
            list(zip(elements.display_parameter_commands, parameters))):
            if parameter:
                command.send_value(32, Line1Text(parameter[0]).as_ascii(),
                                   Line2Text(parameter[1]).as_ascii())
            else:
                command.send_value(33)

    return display


display_specification = DisplaySpecification(create_root_view=create_root_view,
                                             protocol=protocol,
                                             notifications=Notifications)

# okay decompiling ./MIDIRemoteScripts/KeyLab_Essential_mk3/display.pyc
