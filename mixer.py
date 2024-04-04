# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_Essential_mk3\mixer.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1893 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.base import listens, nop
from ableton.v3.control_surface.components import MixerComponent as MixerComponentBase
from ableton.v3.control_surface.components import SessionRingComponent
from ableton.v3.control_surface.components.scroll import ScrollComponent,Scrollable
from ableton.v3.control_surface.controls import ButtonControl,StepEncoderControl
from .PythonBridge import dispatch_hotkey
from .Settings import *
#from .Log import log

class MixerComponent(MixerComponentBase,ScrollComponent,Scrollable):
    part_toggle_button = ButtonControl()
    bank_toggle_button = ButtonControl()
    save_project_button = ButtonControl()
    scroll_encoder = StepEncoderControl(num_steps=64)

    def __init__(self, *a, **k):
        self._session_ring = SessionRingComponent(name="Mixer_Session_Ring",
          num_tracks=8,
          set_session_highlight=nop,
          snap_track_offset=False,
          is_private=True)

        (super().__init__)(a, session_ring=self._session_ring, **k)
        self.add_children(self._session_ring)
        self._MixerComponent__on_tracks_changed.subject = self._session_ring
        self._MixerComponent__on_tracks_changed()
        self.steps = ENCODER_TRACK_BANK_TRACKS_PER_CLICK
        self.bank_toggle_button.color = "Mixer.MuteButton"
        self.bank_toggle_button.on_color = "Mixer.SoloButton"

    def set_part_toggle_button(self, button):
        self.part_toggle_button.set_control_element(button)

    @part_toggle_button.pressed
    def part_toggle_button(self, _):
        self._session_ring.track_offset = 8 if self._session_ring.track_offset == 0 else 0




    def set_bank_toggle_button(self, button):
        self.bank_toggle_button.set_control_element(button)

    @bank_toggle_button.pressed
    def bank_toggle_button(self, _):
        self.bank_bank_toggle_button._is_on = not self.bank_bank_toggle_button._is_on

    @bank_toggle_button.double_clicked
    def bank_bank_toggle_button(self, _):
        old_color = self.bank_bank_toggle_button.color
        self.bank_bank_toggle_button.color = self.bank_bank_toggle_button.on_color
        self.bank_bank_toggle_button.on_color = old_color

    @bank_toggle_button.pressed_delayed
    def bank_bank_toggle_button(self, _):
        pass

    @listens("tracks")
    def __on_tracks_changed(self):
        self.part_toggle_button.enabled = len(self._session_ring.tracks_to_use()) > 8
        self.part_toggle_button.color = "Banking.PageOne" if self._session_ring.track_offset == 0 else "Banking.PageTwo"

    def set_save_project_button(self, button):
        self.save_project_button.set_control_element(button)
        self.save_project_button.color = "SaveProject.On"

    @save_project_button.pressed
    def save_project_button(self, _):
        if PY_SAVE_PROJECT:
            if IS_MAC:
                dispatch_hotkey("command+s")
            else:
                dispatch_hotkey("ctrl+s")

    @scroll_encoder.value
    def scroll_encoder(self, value, _):
        if len(self._session_ring.tracks_to_use()) > 8:
            down = (value < 0) != ENCODER_TRACK_DIRECTION_INVERTED
            #log(f"scroll_encoder: {value} down: {down}")
            if ENABLE_ROUNDTRIP_BANKING_TRACK:
                if not down:
                    self.scroll_up()
                else:
                    self.scroll_down()
            else:
                if down and self.can_scroll_down():
                    self.scroll_down()
                if not down and self.can_scroll_up():
                    self.scroll_up()

    def can_scroll_up(self):
        current_offset = self._session_ring.track_offset
        if len(self._session_ring.tracks_to_use()) >current_offset + self.steps:
            return True
        return False

    def can_scroll_down(self):
        current_offset = self._session_ring.track_offset
        if current_offset > 0:
            return True
        return False

    def scroll_up(self):
        new_offset = self._session_ring.track_offset + self.steps
        if new_offset >= len(self._session_ring.tracks_to_use()):
            new_offset = 0
        self._session_ring.track_offset = new_offset

    def scroll_down(self):
        new_offset = self._session_ring.track_offset - self.steps
        if new_offset < 0:
            new_offset = (len(self._session_ring.tracks_to_use()) // self.steps) * self.steps
        self._session_ring.track_offset = new_offset


# okay decompiling ./MIDIRemoteScripts/KeyLab_Essential_mk3/mixer.pyc
