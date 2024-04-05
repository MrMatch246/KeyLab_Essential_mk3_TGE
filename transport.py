
from ableton.v3.control_surface.components import TransportComponent as TransportComponentBase
from ableton.v3.control_surface.controls import ButtonControl,ToggleButtonControl
from ableton.v3.control_surface.skin import OptionalSkinEntry
from ableton.v3.live import get_bar_length, move_current_song_time
from .Settings import *
from .PythonBridge import dispatch_hotkey

class TransportComponent(TransportComponentBase):
    seek_dict = {
        'color': "Transport.Seek",
        'pressed_color': "Transport.SeekPressed",
        'repeat': True,
        'delay_time': 0}
    rewind_button = ButtonControl(**seek_dict)
    fastforward_button = ButtonControl(**seek_dict)
    play_button = ButtonControl(color="Transport.PlayOff", on_color="Transport.PlayOn")
    stop_button = ButtonControl(color="Transport.StopOff",
                            on_color="Transport.StopOn",
                            pressed_color=(OptionalSkinEntry("Transport.StopPressed")))
    loop_button = ToggleButtonControl(color="Transport.LoopOff",
                                      on_color="Transport.LoopOn")
    def __init__(self, *a, **k):
        super(TransportComponent, self).__init__(*a, **k)
        self.stopped = False
    @rewind_button.pressed
    def rewind_button(self, _):
        move_current_song_time(self.song, -REWIND_FORWARD_SPEED)

    @fastforward_button.pressed
    def fastforward_button(self, _):
        move_current_song_time(self.song, REWIND_FORWARD_SPEED)

    if ENABLE_PLAY_PAUSE_BUTTON:
        @play_button.pressed
        def play_button(self, _):
            if self.song.is_playing:
                self.song.stop_playing()
            else:
                if self.stopped:
                    self.song.start_playing()
                    self.stopped = False
                else:
                    self.song.continue_playing()


        @play_button.pressed_delayed
        def play_button(self, _):
            self.song.start_playing()

        @stop_button.pressed
        def stop_button(self, _):
            self.song.stop_playing()
            self.stopped = True

    if PY_ENABLE_LOOP_SELECTION:
        @loop_button.pressed_delayed
        def loop_button(self, button):
            if IS_MAC:
                dispatch_hotkey("command+l")
            else:
                dispatch_hotkey("ctrl+l")
