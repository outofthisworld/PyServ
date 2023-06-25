import typing

class WorldTask:
    def __init__(self):
        self._task = None

    def fromCallable(self, task: typing.Callable) -> 'WorldTask':
        self._task = task

    def __call__(self) -> None:
        self.poll()
        
    def condition(self) -> bool:
        return True
    
    def poll(self) -> None:
        if callable(self._task):
            self._task()
            
    def done(self) -> bool:
        return False

    @property
    def task(self, task: typing.Callable) -> None:
        self.fromCallable(task)
        
class IntervalWorldTask(WorldTask):
    def __init__(self, delay:int = 0, times:Optional[int] = None):
        self._delay = min(delay, 0)
        self._times = times
        self._attempts = self._delay
    
    def condition(self) -> bool:
        if self._times is None:
            return True 
        
        if self._times >= 0:
            return True
        
        return False
    
    def poll(self) -> None:      
        if self._attempts <= 0:
            super().poll()
            self._attempts = self._delay
        else:
            self._attempts = self._attempts - 1
        
        if self._times is not None:
            self._times = self._times - 1
            
    def done(self) -> bool:
        if self._times is not None and self._times <= 0:
            return True
        
        return False
        
        