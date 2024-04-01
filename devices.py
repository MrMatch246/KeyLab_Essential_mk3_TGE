from __future__ import absolute_import, print_function, unicode_literals

from ableton.v3.base import listenable_property
from ableton.v3.control_surface.components import DeviceBankNavigationComponent
from ableton.v3.control_surface.components import DeviceComponent as DeviceComponentBase
from ableton.v3.control_surface.components import SimpleDeviceNavigationComponent
from ableton.v3.control_surface.controls import ButtonControl
from ableton.v3.control_surface.display import Renderable
from .PythonBridge import dispatch_hotkey
from .Settings import PY_TOGGLE_WRENCH, IS_MAC

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

    def set_bank_toggle_button(self, button):
        self.bank_toggle_button.set_control_element(button)

    @bank_toggle_button.pressed
    def bank_toggle_button(self, _):
        self._bank_provider.index = 2 if self._bank_provider.index == 0 else 0
        self.has_changed_bank_index = True

    def update(self):
        super().update()
        can_bank = self._bank_provider is not None and self._adjusted_bank_count() > 1
        self.bank_index = self._bank_provider.index if can_bank else 0
        self.bank_toggle_button.enabled = can_bank
        if can_bank:
            self.bank_toggle_button.color = "Banking.PageOne" if self._bank_provider.index == 0 else "Banking.PageTwo"
