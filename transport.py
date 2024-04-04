
from ableton.v3.control_surface.components import TransportComponent as TransportComponentBase
from ableton.v3.control_surface.controls import ButtonControl
from ableton.v3.live import get_bar_length, move_current_song_time
from .Settings import *

class TransportComponent(TransportComponentBase):
    seek_dict = {
        'color': "Transport.Seek",
        'pressed_color': "Transport.SeekPressed",
        'repeat': True,
        'delay_time': 0}
    rewind_button = ButtonControl(**seek_dict)
    fastforward_button = ButtonControl(**seek_dict)
    play_button = ButtonControl(color="Transport.PlayOff", on_color="Transport.PlayOn")
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
                self.song.continue_playing()


        @play_button.pressed_delayed
        def play_button(self, _):
            self.song.start_playing()
