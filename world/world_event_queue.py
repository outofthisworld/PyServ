import queue
from typing import TypeVar, Generic

T = TypeVar('T') 

class WorldEventQueue(Generic[T]):
    def __init__(self, **kwargs):
        self._event_queue: queue.Queue[T] = queue.Queue()

    def poll(self):
        temp_queue: queue.Queue[t] = queue.Queue()
    
        while not self._event_queue.empty():
            task = self._event_queue.get(False)
            if task is None:
                continue
            
            task.poll()
            
            if not task.done():
                temp_queue.put(task, False)
                
        self._event_queue = temp_queue
                
                
    @property
    def queue(self):
        return self._event_queue
                
    # override +=         
    def __iadd__(self, task: T) -> None:
        self._event_queue.put(task, True)