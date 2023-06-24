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
        self._server: typing.Optional[asyncio.events.AbstractServer] = None
        self._thread: typing.Optional[threading.Thread] = None
        self._accepting_connections: bool = False
        self._event_emitter: EventEmitter = EventEmitter()
        self._event_loop: typing.Optional[asyncio.BaseEventLoop] = None

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

        self._clean_up()
        return True

    def _clean_up(self) -> None:
        """Perform clean up tasks"""
        try:
            if self._server is not None and self._server.is_serving():
                self._server.close()
                
            if self._event_loop is not None and self._event_loop.is_running():
                self._event_loop.stop()
                
            if self._event_loop is not None and not self._event_loop.is_closed():
                self._event_loop.close()

            self._event_loop = None
            self._thread = None
            self._server = None
            self._accepting_connections = False
            self._clients = []
            self._event_emitter = EventEmitter()
        except Exception as e:
            print(e)

    # dunder methods
    def __del__(self) -> None:
        """Called when the object is destructed or destoryed. Clean up the server"""
        self._clean_up()

    # private methods
    def _start(self) -> None:
        try:
            if self._event_loop is None:
                self._event_loop = asyncio.new_event_loop()
            
            asyncio.set_event_loop(self._event_loop)
            self._event_loop.run_until_complete(self._bind_server())
        finally:
            loop.stop()
            loop.close()
  
    async def _bind_server(self) ->None:
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
            self._clean_up()  # Clean up after

    async def _handle_connection(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        """Establish a connection and listen to it"""
        
        print("accepting connection")
        
        self._clients.append(net.client.Client(reader=reader, writer=writer))
        
        client = self._clients[len(self._clients)-1]

        print("listening to client")
        await client.listen()

        self._event_emitter.emit('connect', client)

    # properties
    @property
    def clients(self) -> typing.List[net.client.Client]:
        """Get the list of clients connected to the server"""
        return [*self._clients]

    @property
    def events(self) -> EventEmitter:
        return self._event_emitter
