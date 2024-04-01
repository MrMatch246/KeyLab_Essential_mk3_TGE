# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_Essential_mk3\elements.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 6123 bytes
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial
from ableton.v3.control_surface import MIDI_NOTE_TYPE, ElementsBase, MapMode, create_button, create_sysex_sending_button
from ableton.v3.control_surface.elements import CachingSendMessageGenerator, DisplayLineElement, EncoderElement, ButtonMatrixElement
from MiniLab_3.encoder import RealigningEncoderMixin
from . import midi
from .display import Line1Text, Line2Text

from .Settings import *


def create_rgb_button(identifier, name=None, **k):
    return create_sysex_sending_button(
 identifier,
 name,
 midi.LED_HEADER + (midi.BUTTON_ID_TO_SYSEX_ID[identifier],), is_rgb=True, **k)


def create_rgb_pad(identifier, name, **k):
    return create_sysex_sending_button(
 identifier,
 name,
 midi.LED_HEADER + (midi.PAD_ID_TO_SYSEX_ID[identifier],), msg_type=MIDI_NOTE_TYPE, 
     is_rgb=True, **k)


class RealigningEncoderElement(RealigningEncoderMixin, EncoderElement):

    def _get_sysex_header(self):
        msg_id = self.message_identifier()
        if msg_id >= 105:
            return
        return midi.ENCODER_VALUE_HEADER + (msg_id - 93,)


class Elements(ElementsBase):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self.add_button(20, "Stop_Button")
        self.add_button(21, "Play_Button")
        self.add_button(22, "Record_Button")

        if TAP_SHIFT_MODE:
            self.add_modifier_button(23, "Tap_Button")
        else:
            self.add_button(23, "Tap_Button")

        self.add_button(24, "Loop_Button")
        self.add_button(25, "Rewind_Button")
        self.add_button(26, "Fastforward_Button")

        if TAP_SHIFT_MODE:
            self.add_modified_control(control=(self.rewind_button),modifier=(self.tap_button),name="previous_device_button")
            self.add_modified_control(control=(self.fastforward_button),modifier=(self.tap_button),name="next_device_button")

        self.add_button(27, "Metronome_Button")
        self.add_button(40, "Save_Button")

        if PY_SAVE_PROJECT:
            self.add_modified_control(control=(self.save_button),modifier=(self.tap_button),name="save_project_button")

        self.add_button(41, "Punch_Button")
        self.add_button(42, "Undo_Button")
        self.add_button(43, "Redo_Button")
        self.add_button(44, "Context_Button_0")
        self.add_button(45, "Context_Button_1")

        if TAP_CONTEXT_1_IS_SOLO and TAP_SHIFT_MODE:
            self.add_modified_control(control=(self.context_button_1),modifier=(self.tap_button),name="target_track_solo_button")

        self.add_button(46, "Context_Button_2")
        self.add_button(47, "Context_Button_3")
        self.add_button(117, "Display_Encoder_Button")
        self.add_button(118, "Bank_Button")

        if ENCODER_DEVICE_BANK:
            self.add_modifier_button(119, "Part_Button")
        else:
            self.add_button(119, "Part_Button")

        if PY_TOGGLE_WRENCH:
            self.add_modified_control(control=(self.part_button),modifier=(self.tap_button),name="wrench_toggle_button")



        self.add_matrix([
            [
                40, 41, 42, 43], [36, 37, 38, 39]],
            "Pad_Bank_A",
            element_factory=create_rgb_pad,
            channels=10)
        self.add_matrix([
            range(44, 52)],
            "Pad_Bank_B", element_factory=create_rgb_pad, channels=10)
        if TAP_SHIFT_MODE and TAP_PADS_MUTE_SOLO:
            #reorder so that pad 5 is the first button
            row=[self.pad_bank_b._orig_buttons[0][i] for i in [4,5,6,7,0,1,2,3]]
            pad_bank_b_reordered = ButtonMatrixElement(rows=[row])
            self.add_modified_control(control=(self.pad_bank_a),modifier=(self.tap_button),name="pad_bank_a_shifted")
            self.add_modified_control(control=(pad_bank_b_reordered),modifier=(self.tap_button),name="pad_bank_b_shifted")



        self.add_element("Encoder_9", RealigningEncoderElement, 104)
        self.add_encoder(113, "Fader_9")
        self.add_encoder(116, "Display_Encoder", map_mode=(MapMode.LinearBinaryOffset))

        if ENCODER_DEVICE_BANK:
            self.add_modified_control(control=(self.display_encoder),modifier=(self.part_button),name="display_encoder_button_part_shifted")

        self.add_matrix([
            list(range(96, 104)) + list(range(105, 113))],
            "Continuous_Controls",
            element_factory=RealigningEncoderElement)
        self.add_submatrix((self.continuous_controls), "Encoders", columns=(0, 8))
        self.add_submatrix((self.continuous_controls), "Faders", columns=(8, 16))
        self.add_sysex_element(midi.PROGRAM_HEADER, "Program_Command")
        self.add_sysex_element((midi.DISPLAY_HEADER),
                               "Display_Full_Screen_Command",
                               send_message_generator=(CachingSendMessageGenerator(midi.make_full_screen_message)),
                               optimized=True)
        self.display_line_1 = DisplayLineElement(name="Display_Line_1",
                                                 display_fn=(lambda message: self.display_full_screen_command.send_value(line1=message)),
                                                 default_formatting=(Line1Text()))
        self.display_line_2 = DisplayLineElement(name="Display_Line_2",
                                                 display_fn=(lambda message: self.display_full_screen_command.send_value(line2=message)),
                                                 default_formatting=(Line2Text()))
        self.add_sysex_element((midi.DISPLAY_HEADER + (1, )),
                               "Display_Header_Command",
                               send_message_generator=(lambda text: midi.make_full_screen_message(1, (0, ), text)),
                               optimized=True)
        self.add_sysex_element((midi.DISPLAY_HEADER + (3, )),
                               "Display_Footer_Command",
                               send_message_generator=(lambda icon1, icon2, icon3, icon4: midi.DISPLAY_HEADER + (3, ) + (16, icon1.state.value, 0, 18, icon1.type.value, 0) + (32, icon2.state.value, 0, 34, icon2.type.value, 0) + (48, icon3.state.value, 0, 50, icon3.type.value, 0) + (64, icon4.state.value, 0, 66, icon4.type.value, 0) + (midi.SYSEX_END,)),
                               optimized=True)
        self.add_sysex_element((midi.DISPLAY_HEADER + (23, )),
                               "Display_Popup_Command",
                               send_message_generator=(partial(midi.make_full_screen_message, 23)),
                               optimized=True)
        self.display_parameter_commands = []
        for (i, element) in enumerate(self.continuous_controls_raw + [self.encoder_9, self.fader_9]):
            self.add_sysex_element((midi.DISPLAY_HEADER + (32, i)),
                                   ("Display_Parameter_Command_{}".format(i)),
                                   send_message_generator=partial((midi.make_full_screen_message),
                                                                  line3=(element.original_identifier())),
                                   optimized=True)
            self.display_parameter_commands.append(getattr(self, "display_parameter_command_{}".format(i)))

    def add_button(self, identifier, name, **k):
        (self.add_element)(
         name, 
         (create_rgb_button if identifier in midi.BUTTON_ID_TO_SYSEX_ID else create_button), 
         identifier, **k)

# okay decompiling ./MIDIRemoteScripts/KeyLab_Essential_mk3/elements.pyc
