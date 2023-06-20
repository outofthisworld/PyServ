import asyncio
from .world import *

class World:
    def __init__(self):
        self._world_event_queue = WorldEventQueue()
        self._world_network_event_pipeline = WorldNetworkListener(world=self)
        self._boot_up_tasks = [
            self.boot_plugins,
            self.load_maps,
            self.load_npcs
        ]

    def _poll():
        # process world events
        self.world_event_queue.poll()

    def boot_plugins():
        pass
    
    def load_maps():
        pass
    
    def load_npcs():
        pass
    
    async def start() -> asyncio.Task[None]:
        return asyncio.create_task(self._start)
    
    def _start():
        self._boot()
        while True:
            self._poll()
    
    def _boot():
       for boot_task in self._boot_up_tasks:
           boot_task()
    
    @property
    def world_event_queue(self):
        return self._world_event_queue
    
    @property
    def world_network_event_pipeline(self):
        return self._world_network_event_pipeline