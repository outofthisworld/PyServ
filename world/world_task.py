import typing
from typing import Optional

class WorldTask:
    def __init__(self):
        self._task = None

    def fromCallable(self, task: typing.Callable) -> 'WorldTask':
        self._task = task

    def __call__(self) -> None:
        self.poll()
    
    def poll(self) -> None:
        if callable(self._task):
            self._task()
            
    def done(self) -> bool:
        return False

    @property
    def task(self, task: typing.Callable) -> None:
        self.fromCallable(task)
        
class IntervalWorldTask(WorldTask):
    def __init__(self, delay:int = 0, initialDelay=False, times:Optional[int] = None):
        self._delay = max(delay, 0)
        self._times = times
        self._attempts = 0 if not initialDelay else self._delay

    def poll(self) -> None: 
        if self._times is not None and self._times <= 0:
            return
        
        if self._attempts > 0:
            self._attempts = self._attempts - 1
            return
            
        super().poll()
        self._attempts = self._delay
        
        if self._times is not None:
            self._times = self._times - 1
            
    def done(self) -> bool:
        if self._times is not None and self._times <= 0:
            return True
        
        return False
        
        