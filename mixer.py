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
from .Settings import PY_SAVE_PROJECT,IS_MAC , ENABLE_ROUNDTRIP_BANKING_TRACK
class MixerComponent(MixerComponentBase,ScrollComponent,Scrollable):
    bank_toggle_button = ButtonControl()
    save_project_button = ButtonControl()
    scroll_encoder = StepEncoderControl(num_steps=64)

    def __init__(self, *a, **k):
        self._session_ring = SessionRingComponent(name="Mixer_Session_Ring",
          num_tracks=8,
          set_session_highlight=nop,
          snap_track_offset=True,
          is_private=True)
        (super().__init__)(a, session_ring=self._session_ring, **k)
        self.add_children(self._session_ring)
        self._MixerComponent__on_tracks_changed.subject = self._session_ring
        self._MixerComponent__on_tracks_changed()

    def set_bank_toggle_button(self, button):
        self.bank_toggle_button.set_control_element(button)

    @bank_toggle_button.pressed
    def bank_toggle_button(self, _):
        self._session_ring.track_offset = 8 if self._session_ring.track_offset == 0 else 0

    @listens("tracks")
    def __on_tracks_changed(self):
        self.bank_toggle_button.enabled = len(self._session_ring.tracks_to_use()) > 8
        self.bank_toggle_button.color = "Banking.PageOne" if self._session_ring.track_offset == 0 else "Banking.PageTwo"

    def set_save_project_button(self, button):
        self.save_project_button.set_control_element(button)

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
            if ENABLE_ROUNDTRIP_BANKING_TRACK:
                if value < 0:
                    self.scroll_down()
                else:
                    self.scroll_up()
            else:
                if value > 0 and self.can_scroll_up():
                    self.scroll_up()
                if value < 0 and self.can_scroll_down():
                    self.scroll_down()

    def can_scroll_up(self):
        current_offset = self._session_ring.track_offset
        if len(self._session_ring.tracks_to_use()) >current_offset + 8:
            return True
        return False

    def can_scroll_down(self):
        current_offset = self._session_ring.track_offset
        if current_offset > 0:
            return True
        return False

    def scroll_up(self):
        new_offset = self._session_ring.track_offset + 8
        if new_offset >= len(self._session_ring.tracks_to_use()):
            new_offset = 0
        self._session_ring.track_offset = new_offset

    def scroll_down(self):
        new_offset = self._session_ring.track_offset - 8
        if new_offset < 0:
            new_offset = (len(self._session_ring.tracks_to_use()) // 8) * 8
        self._session_ring.track_offset = new_offset


# okay decompiling ./MIDIRemoteScripts/KeyLab_Essential_mk3/mixer.pyc
