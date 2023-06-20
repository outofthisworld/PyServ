
from events import EventEmitter
from net.client import Client
from world import WorldTask

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

    def _queue_world_event(self, client, packet_cls, buffer):
        self._world.event_queue.put(WorldTask().fromCallable(packet_cls(
            world=self._world,
            client=client,
            buffer=buffer
        )))
