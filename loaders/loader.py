"""
    Loader
"""
from abc import ABC, abstractmethod
from typing import TypeVar
from events import EventEmitter

T = TypeVar('T')


class Loader(ABC):
    """Loader"""

    def __init__(self):
        """Init"""
        super().__init__()
        self._event_emitter: EventEmitter = EventEmitter()

    def load(self, *args, **kwargs):
        """Load"""
        self._event_emitter.emit('loading')
        result = self._load(*args, **kwargs)
        self._event_emitter.emit('loaded', result)
        return result

    async def load_async(self, *args, **kwargs):
        """Load Async"""
        return self._load(*args, **kwargs)

    @abstractmethod
    def _load(self, *args, **kwargs) -> T:
        """Load"""

    @property
    def events(self):
        """Events"""
        return self._event_emitter
