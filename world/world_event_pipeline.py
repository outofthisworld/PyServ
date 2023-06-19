import queue

class WorldEventPipeline:
    def __init__(self, **kwargs):
        self._world = kwargs.get('world')
        self._event_queue = queue.Queue()

        if not self._world:
            raise ValueError("Invalid args passed to world event pipeline")

    def listen(self, event_pipeline):
        event_pipeline.subscribe(
            'client', self._process_client_packets)

    def _process_client_packets(self, client):
        client.event_emitter.subscribe(
            'packet', self._queue_world_event)

    def _queue_world_event(self, event):
        self._event_queue.put(event) #make this into a task

    def poll(self):
        while self._event_queue.is_not_empty:
            event = self._event_queue.get(False)
            event.Packet(
                world = self._world
                client = event.client
                buffer = event.buffer
            )()
