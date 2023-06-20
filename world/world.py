import asyncio
from world import *

class World:
    def __init__(self):
        self._world_event_queue = WorldEventQueue()
        
    def _poll():
        # process world events
        self.world_event_queue.poll()

    async def start() -> asyncio.Task[None]:
        return asyncio.create_task(self._start)
    
    def _start():
        self._boot()
        while True:
            self._poll()
    
    def _boot():
       pass
    
    @property
    def world_event_queue(self):
        return self._world_event_queue