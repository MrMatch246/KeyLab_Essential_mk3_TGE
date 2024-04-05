from ableton.v3.control_surface.components import TargetTrackComponent as TargetTrackComponentBase
from ableton.v3.live import liveobj_valid, liveobj_changed
class TargetTrackComponent(TargetTrackComponentBase):

    def _target_clip_from_arrangement(self):
        clip = self.song.view.detail_clip
        if liveobj_valid(clip):
            try:
                if clip in self._target_track.arrangement_clips:
                    return clip
            except:
                return None