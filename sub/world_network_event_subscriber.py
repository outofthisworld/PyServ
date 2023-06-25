
from events import EventEmitter, EventHandler
from net.client import Client
from world import WorldTask

class WorldNetworkEventSubscriber():
    def __init__(self, **kwargs):
        self._world = kwargs.get('world')
        if self._world is None:
            raise ValueError("Missing world arg in WorldNetworkListener")

    def listen(self, event_pipeline: EventEmitter):
        event_pipeline.subscribe_class(self)

    @EventHandler(event='client')
    def _process_client_packets(self, client: Client):
        client.event_emitter.subscribe(self)
    
    @EventHandler(event='packet')
    def _queue_world_event(self, client, packet_cls, buffer):
        self._world.event_queue.put(WorldTask().fromCallable(packet_cls(
            world=self._world,
            client=client,
            buffer=buffer
        )))
