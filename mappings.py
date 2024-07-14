# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_Essential_mk3\mappings.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1837 bytes
from __future__ import absolute_import, print_function, unicode_literals

from ableton.v3.control_surface.mode.behaviour import ToggleBehaviour

from .Settings import *


def create_mappings(control_surface):
    mappings = dict()
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

    mappings["Transport"]["tap_tempo_button"] = "metronome_tap_button"

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
                 bank_toggle_button="bank_button"
                 )

    if TAP_CONTEXT_0_IS_MUTE:
        mixer["target_track_mute_button"] = "context_button_0_tap_shifted"

    if TAP_CONTEXT_1_IS_ARM:
        mixer["target_track_arm_button"] = "context_button_1_tap_shifted"
    else:
        mixer["target_track_solo_button"] = "context_button_1_tap_shifted"
    if CONTEXT_1_IS_SOLO:
        mixer["target_track_solo_button"] = "context_button_1"
    else:
        mixer["target_track_arm_button"] = "context_button_1"

    if PY_SAVE_PROJECT:
        mixer["save_project_button"] = "save_project_button"

    if PY_UPDATE_FILESYSTEM:
        mixer["update_filesystem_button"] = "loop_tap_button"

    mixer["scroll_encoder"] = "display_encoder_part_shifted"

    mappings["Mixer"] = mixer

    mappings["Session"] = dict(selected_scene_launch_button="display_encoder_button",clip_launch_buttons="pad_bank_a_shifted")

    mappings["Drum_Group"] = dict(matrix="pad_bank_a")

    mappings["Continuous_Control_Modes"] = dict(
        support_momentary_mode_cycling=False,
        cycle_mode_button="context_button_0",
        device=dict(component="Device",
                    parameter_controls="continuous_controls",
                    prev_button="previous_device_button",
                    next_button="next_device_button",
                    wrench_toggle_button="part_button_tap_shifted",
                    ),
        mixer=dict(component="Mixer", volume_controls="faders",
                   pan_controls="encoders",
                   master_track_volume_control="fader_9",
                   prehear_volume_control="encoder_9",
                   ))


    mappings["Continuous_Control_Modes"]["device"]["bank_scroll_encoder"] = "display_encoder_tap_shifted"




    mappings["Continuous_Pad_Bank_B_Modes"] = dict(
        support_momentary_mode_cycling=False,
        cycle_mode_button="display_encoder_button_part_shifted",
        default_behaviour=ToggleBehaviour(),
        Mixer_Mute=dict(component="Mixer",
                     track_select_buttons="pad_bank_b_row1",
                     mute_buttons="pad_bank_b_row2"),
        Mixer_Solo=dict(component="Mixer",
                     track_select_buttons="pad_bank_b_row1",
                     solo_buttons="pad_bank_b_row2"),
        Mixer_Arm=dict(component="Mixer",
                     track_select_buttons="pad_bank_b_row1",
                     arm_buttons="pad_bank_b_row2"),
    )



    return mappings

# okay decompiling ./MIDIRemoteScripts/KeyLab_Essential_mk3/mappings.pyc
