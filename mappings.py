# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_Essential_mk3\mappings.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1837 bytes
from __future__ import absolute_import, print_function, unicode_literals

from .modSettings import FADER_9_IS_MASTER, TAP_BUTTON_IS_SHIFT_BUTTON, \
    TAP_BUTTON_IS_SHIFT_BUTTON_AND_TAP_BUTTON, CONTEXT_1_WITH_SHIFT_IS_SOLO


def create_mappings(_):
    mappings = {}
    mappings["Modifier_Background"] = dict(shift="shift_button")
    mappings["Transport"] = dict(play_button="play_button",
                                 stop_button="stop_button",
                                 metronome_button="metronome_button",
                                 loop_button="loop_button",
                                 capture_midi_button="save_button",
                                 rewind_button="rewind_button",
                                 fastforward_button="fastforward_button")

    if TAP_BUTTON_IS_SHIFT_BUTTON:
        if TAP_BUTTON_IS_SHIFT_BUTTON_AND_TAP_BUTTON:
            mappings["Transport"]["tap_tempo_button"] = "shift_button"
    else:
        mappings["Transport"]["tap_tempo_button"] = "tap_button"

    mappings["View_Based_Recording"] = dict(record_button="record_button")
    mappings["Undo_Redo"] = dict(undo_button="undo_button",
                                 redo_button="redo_button")
    mappings["Clip_Actions"] = dict(quantize_button="punch_button")
    mappings["View_Control"] = dict(prev_track_button="context_button_2",
                                    next_track_button="context_button_3",
                                    scene_encoder="display_encoder")
    if FADER_9_IS_MASTER:
        mixer = dict(target_track_arm_button="context_button_1",
                     master_track_volume_control="fader_9",
                     prehear_volume_control="encoder_9")
    else:
        mixer = dict(target_track_arm_button="context_button_1",
                     target_track_volume_control="fader_9",
                     target_track_pan_control="encoder_9")
    if TAP_BUTTON_IS_SHIFT_BUTTON and CONTEXT_1_WITH_SHIFT_IS_SOLO:
        mixer["target_track_solo_button"] = "target_track_solo_button"

    mappings["Mixer"] = mixer
    mappings["Session"] = dict(
        selected_scene_launch_button="display_encoder_button",
        clip_launch_buttons="pad_bank_a")
    mappings["Drum_Group"] = dict(matrix="pad_bank_b")
    mappings["Continuous_Control_Modes"] = dict(
        support_momentary_mode_cycling=False,
        cycle_mode_button="context_button_0", device=dict(component="Device",
                                                          parameter_controls="continuous_controls",
                                                          bank_toggle_button="part_button"),
        mixer=dict(component="Mixer", volume_controls="faders",
                   pan_controls="encoders", bank_toggle_button="part_button"))

    if TAP_BUTTON_IS_SHIFT_BUTTON:
        mappings["Continuous_Control_Modes"]["device"]["prev_button"] = "previous_device_button"
        mappings["Continuous_Control_Modes"]["device"]["next_button"] = "next_device_button"

    return mappings

# okay decompiling ./MIDIRemoteScripts/KeyLab_Essential_mk3/mappings.pyc
