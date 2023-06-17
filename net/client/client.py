import typing as types
import asyncio as aio
import net.common as commons

from events import EventEmitter
from packets import incoming_packets, packet

class Client(object):
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
    def stop() -> None:
        self._listening = False

    async def listen(self) -> types.Optional[aio.Task[None]]:
        if self._listening:
            return None

        self._listening = True
        return aio.create_task(self._read_socket)

    # private methods
    async def _read_socket(self) -> None:
        reader, writer = self.reader, self.writer
        while self._listening:
            data = await reader.recv(self.IN_BUF_THRESHOLD)
            self.buffer.add_bytes(data)
            id = self.buffer.read_int(SignType.UNSIGNED)
            if (Packet := incoming_packets.get(id)) is not None:
                self._eventemitter.emit('packet', Packet())

    # properties

    @property
    def reader() -> aio.StreamReader:
        return self._reader

    @property
    def writer() -> aio.StreamWriter:
        return self._writer

    @property
    def buffer() -> commons.ByteBuffer:
        return self._buffer

    @property
    def events() -> EventEmitter:
        return self._eventemitter
