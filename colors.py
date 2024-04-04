# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_Essential_mk3\colors.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 3339 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface import BasicColors
from ableton.v3.control_surface.elements import FallbackColor, create_rgb_color
from ableton.v3.live import liveobj_color_to_midi_rgb_values
from .Log import log
def create_color(r, g, b):
    return create_rgb_color((r, g, b, 32))


def create_blinking_color(r, g, b):
    return create_rgb_color((r, g, b, 2))

def create_dynamic_color_bright(x):
    return create_color(*liveobj_color_to_midi_rgb_values(x))

def create_dynamic_color_dark(x):
    color = liveobj_color_to_midi_rgb_values(x)
    return create_color(*(int(c / 8) for c in color))


class Rgb:
    OFF = FallbackColor(create_color(0, 0, 0), BasicColors.OFF)
    WHITE_HALF = create_color(32, 32, 32)
    WHITE = create_color(127, 127, 127)
    RED = create_color(127, 0, 0)
    RED_HALF = create_color(32, 0, 0)
    RED_LOW = create_color(16, 0, 0)
    RED_BLINK = create_blinking_color(127, 0, 0)
    GREEN = create_color(0, 127, 0)
    GREEN_HALF = create_color(0, 32, 0)
    GREEN_HALF_BLINK = create_blinking_color(0, 32, 0)
    GREEN_BLINK = create_blinking_color(0, 127, 0)
    BLUE = create_color(0, 0, 127)
    BLUE_HALF = create_color(0, 0, 32)
    BLUE_THIRD = create_color(0, 0, 16)
    OCEAN = create_color(20, 80, 127)
    OCEAN_HALF = create_color(10, 40, 64)
    AMBER = create_color(127, 50, 0)
    AMBER_HALF = create_color(20, 5, 0)
    YELLOW = create_color(127, 72, 0)
    YELLOW_HALF = create_color(32, 24, 0)
    YELLOW_LOW = create_color(8, 6, 0)
    PURPLE = create_color(64, 0, 127)
    PURPLE_HALF = create_color(16, 0, 32)
    PURPLE_HALF_BLINK = create_blinking_color(16, 0, 32)


class Skin:

    class DefaultButton:
        On = Rgb.OCEAN_HALF
        Off = Rgb.OCEAN_HALF
        Disabled = Rgb.OFF



    class SaveProject:
        On = Rgb.GREEN_HALF_BLINK
        Off = Rgb.OFF
        Disabled = Rgb.OFF

    class Device:
        On = Rgb.AMBER_HALF
        Navigation = Rgb.PURPLE_HALF
        NavigationPressed = Rgb.PURPLE
        class Wrench:
            On = Rgb.PURPLE
            Off = Rgb.PURPLE_HALF


    class Transport:
        PlayOn = Rgb.GREEN
        PlayOff = Rgb.GREEN_HALF
        StopOn = Rgb.WHITE
        StopOff = Rgb.WHITE_HALF
        LoopOn = Rgb.YELLOW
        LoopOff = Rgb.YELLOW_HALF
        MetronomeOn = Rgb.WHITE
        MetronomeOff = Rgb.WHITE_HALF
        TapTempoPressed = Rgb.WHITE
        TapTempo = Rgb.WHITE_HALF
        SeekPressed = Rgb.WHITE
        Seek = Rgb.WHITE_HALF
        CanCaptureMidi = Rgb.WHITE

    class Recording:
        ArrangementRecordOn = Rgb.RED
        ArrangementRecordOff = Rgb.RED_HALF
        SessionRecordOn = Rgb.RED
        SessionRecordTransition = Rgb.RED_BLINK
        SessionRecordOff = Rgb.RED_HALF

    class UndoRedo:
        UndoPressed = Rgb.WHITE
        Undo = Rgb.WHITE_HALF
        RedoPressed = Rgb.WHITE
        Redo = Rgb.WHITE_HALF

    class ClipActions:
        Quantize = Rgb.WHITE_HALF
        QuantizePressed = Rgb.WHITE

    class ViewControl:
        TrackPressed = Rgb.WHITE
        Track = Rgb.WHITE_HALF

    class ViewToggle:
        SessionOn = Rgb.WHITE
        SessionOff = Rgb.WHITE_HALF

    class Mixer:
        ArmOn = Rgb.RED
        ArmOff = Rgb.RED_HALF
        NoTrack = Rgb.OFF
        TrackSelected = Rgb.WHITE
        SoloOn = Rgb.BLUE
        SoloOff = Rgb.BLUE_THIRD
        MuteOn = Rgb.YELLOW
        MuteOff = Rgb.YELLOW_LOW
        Selected = create_dynamic_color_bright
        NotSelected = create_dynamic_color_dark
        SoloButton = Rgb.BLUE
        MuteButton = Rgb.YELLOW


    class Session:
        Slot = Rgb.OFF
        SlotRecordButton = Rgb.RED_LOW
        NoSlot = Rgb.OFF
        ClipStopped = lambda x: create_color(*liveobj_color_to_midi_rgb_values(x))
        ClipTriggeredPlay = Rgb.GREEN_BLINK
        ClipTriggeredRecord = Rgb.RED_BLINK
        ClipPlaying = Rgb.GREEN
        ClipRecording = Rgb.RED

    class DrumGroup:
        PadEmpty = Rgb.WHITE_HALF
        PadFilled = lambda x: create_color(*liveobj_color_to_midi_rgb_values(x))
        PadSelected = Rgb.OCEAN
        PadMuted = Rgb.AMBER
        PadMutedSelected = Rgb.OCEAN
        PadSoloed = Rgb.BLUE
        PadSoloedSelected = Rgb.OCEAN
        PadPressed = Rgb.WHITE

    class Banking:
        PageOne = Rgb.RED_HALF
        PageTwo = Rgb.RED

    class ModifierBackground:
        Shift = Rgb.OCEAN_HALF
        ShiftPressed = Rgb.OCEAN
        Part = Rgb.OCEAN_HALF
        PartPressed = Rgb.OCEAN
        Bank = Rgb.RED_HALF
        BankPressed = Rgb.RED


    class ContinuousControlModes:

        class Device:
            On = Rgb.PURPLE_HALF

        class Mixer:
            On = Rgb.GREEN_HALF
            Selected = Rgb.WHITE
            NotSelected = lambda x: create_color(*liveobj_color_to_midi_rgb_values(x))
            Off = Rgb.OFF

# okay decompiling ./MIDIRemoteScripts/KeyLab_Essential_mk3/colors.pyc
