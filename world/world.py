from .world import *

class World:
    def __init__(self):
        self._world_event_pipeline = WorldEventPipeline(world=self)


    def _poll():
        # process world events
        self.world_event_pipeline.poll()

    
    @property
    def world_event_pipeline(self):
        return self._world_event_pipeline