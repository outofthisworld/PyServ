import threading
import socket
import contextlib
import struct
import asyncio
import typing
import enum
import net.client

class Server(object):
    def __init__(self, **kwargs):
        """Set up server"""

        # settings
        self.host: str = kwargs.get('host', 'localhost')
        self.port: int = kwargs.get('port', 5005)

        # private
        self._server: asyncio.events.AbstractServer = None
        self._thread: threading.Thread = None
        self._accepting_connections: bool = False

        # private but exposed publicly
        self._clients: list = []

    # methods
    async def start(self) -> bool:
        """Public method starting the server"""

        if self._accepting_connections:
            return False

        self._accepting_connections = True
        self._thread = threading.Thread(target=self._start)
        self._thread.start()
        return True

    async def stop(self) -> bool:
        """Stop the server"""
        if not self._accepting_connections:
            return False

        await self.clean_up()
        return True

    async def clean_up() -> None:
        """Perform clean up tasks"""
        if self._server is not None and self._server.is_serving():
            self._server.close()
            await self._server.wait_closed()

        self._thread = None
        self._server = None
        self._accepting_connections = False

    # dunder methods
    def __del__(self) -> None:
        """Called when the object is destructed or destoryed. Clean up the server"""
        asyncio.create_task(self.clean_up())

    # private methods
    async def _start(self) -> None:
        """Start listening"""
        async with _bind() as server:
            await server.serve_forever()

    @contextlib.asynccontextmanager
    async def _bind(self) -> typing.Generator[asyncio.events.AbstractServer, None, None]:
        """Create async server, bind the connection handler inside a async context manager"""
        try:
            self._server = await asyncio.start_server(self._handle_connection, self.host, self.port)
            yield self._server
        finally:
            await self.clean_up()  # Clean up after

    async def _handle_connection(self, reader, writer) -> None:
        """Establish a connection and listen to it"""
        client = net.client.Client(reader=reader, writer=writer)
        self.clients.append(client)
        client.listen()

    # properties
    @property
    def clients() -> typing.List[net.client.Client]:
        """Get the list of clients connected to the server"""
        return [*self.clients]
