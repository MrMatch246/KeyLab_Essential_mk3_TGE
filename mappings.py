# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_Essential_mk3\mappings.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1837 bytes
from __future__ import absolute_import, print_function, unicode_literals

from .Settings import *


def create_mappings(control_surface):
    mappings = {}
    mappings["Modifier_Background"] = dict(shift="tap_button",
                                           part="part_button",
                                           bank="bank_button")
    mappings["Transport"] = dict(play_button="play_button",
                                 stop_button="stop_button",
                                 metronome_button="metronome_button",
                                 loop_button="loop_button",
                                 capture_midi_button="save_button",
                                 rewind_button="rewind_button",
                                 fastforward_button="fastforward_button")

    if TAP_SHIFT_MODE is TAP_DUAL_MODE:
        mappings["Transport"]["tap_tempo_button"] = "tap_button"

    mappings["View_Based_Recording"] = dict(record_button="record_button")
    mappings["Undo_Redo"] = dict(undo_button="undo_button",
                                 redo_button="redo_button")
    mappings["Clip_Actions"] = dict(quantize_button="punch_button")
    mappings["View_Control"] = {}
    if SCENE_TRACK_NAVIGATION_SWITCH:
        mappings["View_Control"]["track_encoder"] = "display_encoder"
        mappings["View_Control"]["next_scene_button"] = "context_button_3"
        mappings["View_Control"]["prev_scene_button"] = "context_button_2"
    else:
        mappings["View_Control"]["prev_track_button"] = "context_button_2"
        mappings["View_Control"]["next_track_button"] = "context_button_3"
        mappings["View_Control"]["scene_encoder"] = "display_encoder"

    mixer = dict(target_track_arm_button="context_button_1",
                 target_track_volume_control="fader_9",
                 target_track_pan_control="encoder_9",
                 bank_toggle_button="bank_button",
                 )

    if TAP_CONTEXT_1_IS_SOLO:
        mixer["target_track_solo_button"] = "target_track_solo_button"

    if TAP_PADS_MUTE_SOLO:
        mixer["mute_buttons"] = "pad_bank_a_shifted"
        mixer[
            "solo_buttons"] = "pad_bank_b_shifted"  # mixer["track_select_buttons"] = "pad_bank_b_row1_tap_shifted"

    if PY_SAVE_PROJECT:
        mixer["save_project_button"] = "save_project_button"

    if ENCODER_TRACK_BANK_TAP:
        mixer["scroll_encoder"] = "display_encoder_button_tap_shifted"

    mappings["Mixer"] = mixer
    mappings["Session"] = dict(
        selected_scene_launch_button="display_encoder_button",
        clip_launch_buttons="pad_bank_a")
    mappings["Drum_Group"] = dict(matrix="pad_bank_b")
    mappings["Continuous_Control_Modes"] = dict(
        support_momentary_mode_cycling=False,
        cycle_mode_button="context_button_0", device=dict(component="Device",
                                                          parameter_controls="continuous_controls",
                                                          wrench_toggle_button="wrench_toggle_button",
                                                          bank_scroll_encoder="display_encoder_button_part_shifted"),
        mixer=dict(component="Mixer", volume_controls="faders",
                   pan_controls="encoders",
                   track_select_buttons="pad_bank_a_part_shifted",
                   arm_buttons="pad_bank_b_part_shifted",
                   )
    )
    if ENCODER_DEVICE_BANK:
        mappings["Continuous_Control_Modes"]["device"][
            "bank_scroll_encoder"] = "display_encoder_button_part_shifted"
    else:
        mappings["Continuous_Control_Modes"]["device"][
            "part_toggle_button"] = "part_button"

    if ENCODER_TRACK_BANK:
        mappings["Continuous_Control_Modes"]["mixer"][
            "scroll_encoder"] = "display_encoder_button_part_shifted"
    else:
        mappings["Continuous_Control_Modes"]["mixer"][
            "part_toggle_button"] = "part_button"

    if TAP_DEVICE_NAVIGATION:
        mappings["Continuous_Control_Modes"]["device"][
            "prev_button"] = "previous_device_button"
        mappings["Continuous_Control_Modes"]["device"][
            "next_button"] = "next_device_button"

    if PY_TOGGLE_WRENCH:
        mappings["Continuous_Control_Modes"]["device"][
            "wrench_toggle_button"] = "wrench_toggle_button"

    if FADER_9_IS_MASTER:
        mappings["Continuous_Control_Modes"]["mixer"][
            "master_track_volume_control"] = "fader_9"
        mappings["Continuous_Control_Modes"]["mixer"][
            "prehear_volume_control"] = "encoder_9"

    return mappings

# okay decompiling ./MIDIRemoteScripts/KeyLab_Essential_mk3/mappings.pyc
