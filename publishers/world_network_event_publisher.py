
from events import EventEmitter
from net.client import Client

class WorldNetworkEventPublisher():
    def __init__(self, **kwargs):
        self._world = kwargs.get('world')
        if self._world is None:
            raise ValueError("Missing world arg in WorldNetworkListener")

    def listen(self, event_pipeline: EventEmitter):
        event_pipeline.subscribe(
            'client', self._process_client_packets)

    def _process_client_packets(self, client: Client):
        client.event_emitter.subscribe(
            'packet', self._queue_world_event)

    def _queue_world_event(self, event):
        self._world.event_queue.put(WorldTask().fromCallable(event.Packet(
            world=self._world,
            client=event.client,
            buffer=event.buffer
        )))
