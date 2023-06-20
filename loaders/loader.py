"""
    Loader
"""
import abc
import typing
from events import EventEmitter

T = typing.TypeVar('T')


class Loader(abc.ABC):
    """
        Loader
    """
    def __init__(self):
        super().__init__()
        self._event_emitter: EventEmitter = EventEmitter()
        
    async def load(self, *args, **kwargs):
        """
            Load the thing
        """
        self._event_emitter.emit('loading')
        result = await self._load(*args, **kwargs)
        self._event_emitter.emit('loaded', result)
        return result
        
    @abc.abstractmethod
    async def _load(self, *args, **kwargs) -> T:
        """
            Load the thing
        """
        pass
        
    @property
    def events(self):
        return self._event_emitter
