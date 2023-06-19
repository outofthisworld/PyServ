import threading
import contextlib
import asyncio
import typing
import net.client
from events import EventEmitter

class Server(object):
    def __init__(self, **kwargs: dict):
        """Set up server"""

        # settings
        self.host: str = kwargs.get('host', 'localhost')
        self.port: int = kwargs.get('port', 5005)

        # private
        self._server: asyncio.events.AbstractServer = None
        self._thread: threading.Thread = None
        self._accepting_connections: bool = False
        self._event_emitter: EventEmitter = EventEmitter()

        # private but exposed publicly
        self._clients: list = []

    # methods
    async def start(self) -> bool:
        """Public method starting the server"""

        if self._accepting_connections:
            return False

        self._accepting_connections: bool = True
        self._thread: threading.Thread = threading.Thread(target=self._start)
        self._thread.start()
        return True

    async def stop(self) -> bool:
        """Stop the server"""
        if not self._accepting_connections:
            return False

        await self.clean_up()
        return True

    async def clean_up(self) -> None:
        """Perform clean up tasks"""
        if self._server is not None and self._server.is_serving():
            self._server.close()
            await self._server.wait_closed()

        self._thread = None
        self._server = None
        self._accepting_connections = False
        self._clients = []

    # dunder methods
    def __del__(self) -> None:
        """Called when the object is destructed or destoryed. Clean up the server"""
        asyncio.create_task(self.clean_up())

    # private methods
    async def _start(self) -> None:
        """Start listening"""
        async with self._bind() as server:
            await server.serve_forever()

    @contextlib.asynccontextmanager
    async def _bind(self) -> typing.Generator[asyncio.events.AbstractServer, None, None]:
        """Create async server, bind the connection handler inside a async context manager"""
        try:
            self._server = await asyncio.start_server(self._handle_connection, self.host, self.port)
            yield self._server
        finally:
            await self.clean_up()  # Clean up after

    async def _handle_connection(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        """Establish a connection and listen to it"""
        self.clients.append(net.client.Client(reader=reader, writer=writer))
        
        client = self.clients[len(self.clients)-1]

        client.listen()

        self._event_emitter.emit('connect', client)

    # properties
    @property
    def clients(self) -> typing.List[net.client.Client]:
        """Get the list of clients connected to the server"""
        return [*self.clients]

    @property
    def event_emitter(self) -> EventEmitter:
        return self._event_emitter
