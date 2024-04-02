from __future__ import absolute_import, print_function, unicode_literals

from ableton.v3.base import listenable_property
from ableton.v3.control_surface.components import DeviceBankNavigationComponent
from ableton.v3.control_surface.components import DeviceComponent as DeviceComponentBase
from ableton.v3.control_surface.components import SimpleDeviceNavigationComponent
from ableton.v3.control_surface.controls import ButtonControl, StepEncoderControl
from ableton.v3.control_surface.display import Renderable
from .PythonBridge import dispatch_hotkey
from .Settings import PY_TOGGLE_WRENCH, IS_MAC,ENABLE_ROUNDTRIP_BANKING_PARAM

class DeviceControlsComponent(DeviceComponentBase,
                              SimpleDeviceNavigationComponent):
    wrench_toggle_button = ButtonControl()

    def __init__(self, *a, **k):
        super(DeviceControlsComponent, self).__init__(*a, **k)

    def set_wrench_toggle_button(self, button):
        self.wrench_toggle_button.set_control_element(button)

    @wrench_toggle_button.pressed
    def wrench_toggle_button(self, _):
        self._toggle_device_view()

    def _toggle_device_view(self):
        if PY_TOGGLE_WRENCH:
            if IS_MAC:
                dispatch_hotkey("command+alt+p")
            else:
                dispatch_hotkey("ctrl+alt+p")



class DeviceBankToggleComponent(DeviceBankNavigationComponent, Renderable):
    bank_index = listenable_property.managed(0)
    has_changed_bank_index = listenable_property.managed(False)
    bank_toggle_button = ButtonControl()
    scroll_encoder = StepEncoderControl(num_steps=64)

    def set_bank_toggle_button(self, button):
        self.bank_toggle_button.set_control_element(button)

    @bank_toggle_button.pressed
    def bank_toggle_button(self, _):
        if True:
            self._bank_provider.index = 1 if self._bank_provider.index == 0 else 0
            self.has_changed_bank_index = True
    @scroll_encoder.value
    def scroll_encoder(self, value, _):
        if self._bank_provider and self._bank_provider.bank_count() > 1:
            if ENABLE_ROUNDTRIP_BANKING_PARAM:
                if value < 0:
                    self.scroll_down()
                else:
                    self.scroll_up()
            else:
                if value > 0 and self.can_scroll_up():
                    self.scroll_up()
                if value < 0 and self.can_scroll_down():
                    self.scroll_down()

    def scroll_up(self):
        new_index = self._bank_provider.index + 1
        if new_index >= self._bank_provider.bank_count():
            new_index = 0
        self._bank_provider.index = new_index
        self.has_changed_bank_index = True
        self._notify_bank_name()

    def scroll_down(self):
        new_index = self._bank_provider.index - 1
        if new_index < 0:
            new_index = self._bank_provider.bank_count() - 1
        self._bank_provider.index = new_index
        self.has_changed_bank_index = True
        self._notify_bank_name()

    def update(self):
        super().update()
        can_bank = self._bank_provider is not None and self._adjusted_bank_count() > 1
        self.bank_index = self._bank_provider.index if can_bank else 0
        self.bank_toggle_button.enabled = can_bank
        if can_bank:
            self.bank_toggle_button.color = "Banking.PageOne" if self._bank_provider.index == 0 else "Banking.PageTwo"
