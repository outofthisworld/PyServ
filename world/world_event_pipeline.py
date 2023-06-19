class WorldEventPipeline:
    def __init__(self, **kwargs):
        self._server = kwargs.get('server')
        self._world = kwargs.get('world')

        if not self._server or not self._world:
            raise ValueError("Invalid args passed to world event pipeline")
        self._init()

    def _init(self):
        self._server.event_emitter.subscribe(
            'client', self._process_client_packets)

    def _process_client_packets(self, client):
        client.event_emitter.subscribe(
            'packet', self._queue_world_event)

    def _queue_world_event(self, packet):
        self._world.events.process(packet)
