from __future__ import absolute_import, print_function, unicode_literals

from typing import cast
from ableton.v3.base import listenable_property
from ableton.v3.live import liveobj_valid
from ableton.v3.control_surface.components import DeviceBankNavigationComponent
from ableton.v3.control_surface.components import DeviceComponent as DeviceComponentBase
from ableton.v3.control_surface.components import SimpleDeviceNavigationComponent
from ableton.v3.control_surface.controls import ButtonControl, StepEncoderControl,ToggleButtonControl
from ableton.v3.control_surface.display import Renderable
from .PythonBridge import dispatch_hotkey
from .Settings import PY_TOGGLE_WRENCH, IS_MAC,ENABLE_ROUNDTRIP_BANKING_PARAM
#from .Log import log
class DeviceControlsComponent(DeviceComponentBase,
                              SimpleDeviceNavigationComponent):
    wrench_toggle_button = ButtonControl()
    device_button = ToggleButtonControl()


    def __init__(self, *a, **k):
        super(DeviceControlsComponent, self).__init__(*a, **k)
        self.locked_to_device= False
        self.locked_device_name = ""

    def set_wrench_toggle_button(self, button):
        self.wrench_toggle_button.set_control_element(button)
        self.wrench_toggle_button.color = "Device.Wrench.Off"
        self.wrench_toggle_button.on_color = "Device.Wrench.On"

    @wrench_toggle_button.pressed
    def wrench_toggle_button(self, _):
        self._toggle_device_view()

    def _toggle_device_view(self):
        if PY_TOGGLE_WRENCH:
            if IS_MAC:
                dispatch_hotkey("command+alt+p")
            else:
                dispatch_hotkey("ctrl+alt+p")

    @device_button.toggled
    def device_button(self, *_):
        pass
    @device_button.pressed
    def device_button(self, *_):
        pass

    @device_button.double_clicked
    def device_button(self, *k):
        #This is a fix if you unlocked on an empty track and want to lock the device again that was previously locked
        if liveobj_valid(self.device):
            if self.locked_device_name == cast(str, self.device.name) and not self.locked_to_device:
                self._toggle_lock()
                self._toggle_lock()
                self.locked_to_device = True
                self.notify(self.notifications.Device.lock, cast(str, self.device.name),False)
                self._show_message(f"Device Lock On {self.locked_device_name}")
                return

        if not self.locked_to_device :
            if liveobj_valid(self.device):
                self._toggle_lock()
                self.notify(self.notifications.Device.lock, cast(str, self.device.name),True)
                self.locked_device_name = cast(str, self.device.name)
                self._show_message(f"Device Lock On {self.locked_device_name}")
                self.locked_to_device = True
        else:
            self._device_provider.unlock_from_device()
            self.locked_to_device = False
            self._show_message(f"Device Lock Off {self.locked_device_name}")

        self.update()

    def set_part_toggle_button(self, button):
        self.part_toggle_button.set_control_element(button)



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
                if value > 0:
                    self.scroll_up()
                else:
                    self.scroll_down()
            else:
                if value < 0 and self.can_scroll_down():
                    self.scroll_down()
                if value > 0 and self.can_scroll_up():
                    self.scroll_up()

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
