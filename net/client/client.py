from typing import Optional
from asyncio import StreamReader, StreamWriter, Task, create_task
from net.common import ByteBuffer, SignType

from events import EventEmitter
from net.packets import incoming_packets


class Client():
    """Client"""
    IN_BUF_THRESHOLD = 1024

    def __init__(self, **kwargs):
        """Init"""
        self._reader: StreamReader = kwargs.get('reader')
        self._writer: StreamWriter = kwargs.get('writer')

        if not self.reader or not self.writer:
            raise ValueError("Keyword arg (reader|writer) is missing")

        self._listening: bool = False
        self._buffer: ByteBuffer = ByteBuffer()
        self._eventemitter = EventEmitter()

    # methods
    def stop(self) -> None:
        """Stop"""
        self._listening = False

    async def listen(self) -> Optional[Task[None]]:
        """Listen"""
        if self._listening:
            return None

        self._listening = True
        return create_task(self._read_socket())

    # private methods
    async def _read_socket(self) -> None:
        """Read Socket"""
        while self._listening:
            data = await self.reader.read(self.IN_BUF_THRESHOLD)
          
            if(len(data) == 0):
                continue
            
            self._buffer.add_bytes(data)
            
            if (len(self._buffer) < 4):
                continue

            packet_id = self._buffer.read_int(SignType.UNSIGNED)
            packet = incoming_packets.get(packet_id)

            if packet is None:
                self._buffer.clear()
                continue

            if (len(self._buffer) < packet.size):
                self._buffer.rewind()
                continue

            self._eventemitter.emit(
                'packet', self, packet, self._buffer.chunk(
                packet.size))

    # properties

    @property
    def reader(self) -> StreamReader:
        """StreamReader"""
        return self._reader

    @property
    def writer(self) -> StreamWriter:
        """StreamWriter"""
        return self._writer

    @property
    def events(self) -> EventEmitter:
        """EventEmitter"""
        return self._eventemitter
