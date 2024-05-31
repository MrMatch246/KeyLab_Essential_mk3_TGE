# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_Essential_mk3\__init__.py
# Compiled at: 2024-02-20 00:54:37
# Size of source mod 2**32: 2991 bytes
from __future__ import absolute_import, print_function, unicode_literals

from functools import partial

from MiniLab_3 import DrumGroupComponent
from ableton.v3.base import listens
from ableton.v3.control_surface import ControlSurface, \
    ControlSurfaceSpecification, create_skin
from ableton.v3.control_surface.capabilities import CONTROLLER_ID_KEY, NOTES_CC, \
    PORTS_KEY, SCRIPT, controller_id, inport, outport


from .PythonBridge import KeystrokeProxie, setup_requirements, start_server
from .Settings import I_HAVE_PYTHON_3, ENABLE_AUTO_ARM
from .colors import Rgb, Skin
from .devices import DeviceBankToggleComponent, DeviceControlsComponent
from .display import display_specification
from .elements import Elements
from .mappings import create_mappings
from .midi import CONNECTION_MESSAGE, DAW_PROGRAM_BYTE, DISCONNECTION_MESSAGE, \
    REQUEST_PROGRAM_MESSAGE
from .mixer import MixerComponent
from .transport import TransportComponent
from .target_track import TargetTrackComponent



def get_capabilities():
    return {CONTROLLER_ID_KEY: (
        controller_id(vendor_id=7285, product_ids=[588, 652, 716],
                      model_name=["KL Essential 49 mk3", "KL Essential 61 mk3",
                                  "KL Essential 88 mk3"])),

        PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT]), inport(props=[NOTES_CC]),
                    outport(props=[NOTES_CC, SCRIPT]),
                    outport(props=[NOTES_CC])]}


def create_instance(c_instance):
    return KeyLab_Essential_mk3(c_instance=c_instance)


class Specification(ControlSurfaceSpecification):
    elements_type = Elements
    control_surface_skin = create_skin(skin=Skin, colors=Rgb)
    num_tracks = 4
    num_scenes = 2
    link_session_ring_to_track_selection = True
    link_session_ring_to_scene_selection = True
    target_track_component_type = TargetTrackComponent
    include_auto_arming = True
    identity_response_id_bytes = (0, 32, 107, 2, 0, 5)
    create_mappings_function = create_mappings
    hello_messages = (CONNECTION_MESSAGE, REQUEST_PROGRAM_MESSAGE)
    goodbye_messages = (DISCONNECTION_MESSAGE,)
    component_map = {'Device': partial(DeviceControlsComponent, bank_size=16,
                                       bank_navigation_component_type=DeviceBankToggleComponent),
                     'Drum_Group': DrumGroupComponent, 'Mixer': MixerComponent,
                     'Transport': TransportComponent}
    display_specification = display_specification


class KeyLab_Essential_mk3(ControlSurface):

    def __init__(self, *a, **k):
        (super().__init__)(Specification, *a, **k)

    def setup(self):
        super().setup()
        if I_HAVE_PYTHON_3:
            setup_requirements()
            start_server()
        self._KeyLab_Essential_mk3__on_firmware_program_changed.subject = self.elements.program_command

    @listens("value")
    def __on_firmware_program_changed(self, value):
        if value[0] == DAW_PROGRAM_BYTE:
            for encoder in self.elements.continuous_controls_raw:
                encoder.realign_value()

            self.elements.encoder_9.realign_value()
            self.set_can_auto_arm(ENABLE_AUTO_ARM)

    def __del__(self):
        if I_HAVE_PYTHON_3:
            KeystrokeProxie().shutdown()
        super().__del__()

# okay decompiling ./MIDIRemoteScripts/KeyLab_Essential_mk3/__init__.pyc
