import asyncio
from world import *
from loaders.py_plugin_loader import PyPluginLoader
import config.world

class World:
    def __init__(self):
        self._world_event_queue = WorldEventQueue()
        
    def _poll():
        # process world events
        self.world_event_queue.poll()

    async def start() -> asyncio.Task[None]:
        return asyncio.create_task(self._start)
    
    async def _start():
        await self._boot()
        
        while True:
            self._poll()
    
    async def _boot():
       plugin_loader = PyPluginLoader()
       await plugin_loader.loadAsync(config.world.get_plugin_base_dir())
       await plugin_loader.boot(self)
    
    @property
    def world_event_queue(self):
        return self._world_event_queue