
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
    @rewind_button.pressed
    def rewind_button(self, _):
        move_current_song_time(self.song, -REWIND_FORWARD_SPEED)

    @fastforward_button.pressed
    def fastforward_button(self, _):
        move_current_song_time(self.song, REWIND_FORWARD_SPEED)