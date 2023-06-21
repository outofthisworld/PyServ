import asyncio
from world import *
from loaders.py_plugin_loader import PyPluginLoader
import config.world


class World:
    def __init__(self):
        """Init"""
        self._world_event_queue = WorldEventQueue()

    def _poll(self):
        """Poll"""
        # process world events
        self.world_event_queue.poll()

    async def start(self) -> asyncio.Task[None]:
        """Start"""
        return asyncio.create_task(self._start)

    async def _start(self):
        """Start"""
        await self._boot()

        while True:
            self._poll()

    async def _boot(self):
        """Boot"""
        plugin_loader = PyPluginLoader()
        await plugin_loader.load_async(config.world.get_plugin_base_dir())
        await plugin_loader.boot(self)

    @property
    def world_event_queue(self):
        """World Event Queue"""
        return self._world_event_queue
