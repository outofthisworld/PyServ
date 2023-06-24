import asyncio
from .world_event_queue import WorldEventQueue
from loaders.py_plugin_loader import PyPluginLoader
from config.app import PLUGINS_DIR


class World:
    """World"""

    def __init__(self):
        """Init"""
        self._world_event_queue = WorldEventQueue()

    def _poll(self):
        """Poll"""
        # process world events
        self.world_event_queue.poll()

    async def start(self) -> asyncio.Task[None]:
        """Start"""
        return asyncio.create_task(self._start())

    async def _start(self):
        """Start"""
        await self._boot()

        while True:
            self._poll()

    async def _boot(self):
        """Boot"""

        async def load_plugins():
            plugin_loader = PyPluginLoader()
            await plugin_loader.load_async(PLUGINS_DIR)
            await plugin_loader.boot_async(self)

        await asyncio.gather(load_plugins())

    @property
    def world_event_queue(self):
        """World Event Queue"""
        return self._world_event_queue
