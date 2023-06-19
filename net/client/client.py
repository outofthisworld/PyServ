import typing as types
import asyncio as aio
import net.common as commons

from events import EventEmitter
from net.packets import incoming_packets


class Client():
    """
        Client
    """
    IN_BUF_THRESHOLD = 1024

    def __init__(self, **kwargs):
        self._reader: aio.StreamReader = kwargs.get('reader')
        self._writer: aio.StreamWriter = kwargs.get('writer')

        if not self.reader or not self.writer:
            raise ValueError("Keyword arg (reader|writer) is missing")

        self._listening: bool = False
        self._buffer: commons.ByteBuffer = commons.ByteBuffer()
        self._eventemitter = EventEmitter()

    # methods
    def stop(self) -> None:
        """
            Stops listening to the StreamReader
        """
        self._listening = False

    async def listen(self) -> types.Optional[aio.Task[None]]:
        """
            Begins listening and reading data from the StreamReader
        """
        if self._listening:
            return None

        self._listening = True
        return aio.create_task(self._read_socket)

    # private methods
    async def _read_socket(self) -> None:
        """
            Processes incoming data from the StreamReader
        """
        reader, writer = self.reader, self.writer

        buffer: commons.ByteBuffer = commons.ByteBuffer()

        while self._listening:
            buffer.add_bytes(await reader.recv(self.IN_BUF_THRESHOLD))

            if (len(buffer) < 4):
                continue

            id = buffer.read_int(commons.SignType.UNSIGNED)
            packet = incoming_packets.get(id)

            if packet is None:
                print(f"Unhandled packet {id}")
                buffer.clear()
                continue

            if (len(buffer) < packet.size):
                continue

            self._eventemitter.emit('packet', packet())
            buffer.clear()

    # properties

    @property
    def reader(self) -> aio.StreamReader:
        """
            Returns the StreamReader
        """
        return self._reader

    @property
    def writer(self) -> aio.StreamWriter:
        """
            Returns the StreamWriter
        """
        return self._writer

    @property
    def events(self) -> EventEmitter:
        """
            Returns the EventEmitter
        """
        return self._eventemitter
