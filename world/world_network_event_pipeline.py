import queue

class WorldTask:
    def __init__(self):
        self._task = task

    def fromCallable(self, task: Callable) -> 'WorldTask':
        self._task = task

    def __call__(self) -> None:
        self.poll()
    
    def poll(self) -> None:
        if callable(self._task):
            self._task()

    @property
    def task(self, task: Callable) -> None:
        self.withTask(task)


class WorldEventQueue:
    def __init__(self, **kwargs):
        self._event_queue = queue.Queue()
        
    def poll(self):
        while self._event_queue.is_not_empty:
            task = self._event_queue.get(False)
            if task is not None:
                task.poll()

class WorldNetworkListener():
    def __init__(self, **kwargs):
        self._world = kwargs.get('world')
        if self._world is None:
            raise ValueError("Missing world arg in WorldNetworkListener")
    
    def listen(self, event_pipeline):
        event_pipeline.subscribe(
            'client', self._process_client_packets)

    def _process_client_packets(self, client):
        client.event_emitter.subscribe(
            'packet', self._queue_world_event)

    def _queue_world_event(self, event):
        self._world.event_queue.put(WorldTask().fromCallable(event.Packet(
                world = self._world
                client = event.client
                buffer = event.buffer
        )))
            
