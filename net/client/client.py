import typing
import asyncio
import net.common

class Client(object):
    IN_BUF_THRESHOLD = 1024

    def __init__(self, **kwargs):
        self._reader: asyncio.StreamReader = kwargs.get('reader')
        self._writer: asyncio.StreamWriter = kwargs.get('writer')

        if not self.reader or not self.writer:
            raise ValueError("Keyword arg (reader|writer) is missing")

        self._listening: bool = False
        self._buffer: net.common.ByteBuffer = net.common.ByteBuffer()

    # methods
    def stop() -> None:
        self._listening = False

    async def listen(self) -> typing.Optional[asyncio.Task[None]]:
        if self._listening:
            return None

        self._listening = True
        return asyncio.create_task(self._read_socket)

    # private methods
    async def _read_socket(self) -> None:
        reader, writer = self.reader, self.writer
        while self._listening:
            data = await reader.recv(self.IN_BUF_THRESHOLD)
            self.buffer.add_bytes(data)
            id = self.buffer.read_int(SignType.UNSIGNED)
            

    # properties
    @property
    def reader() -> asyncio.StreamReader:
        return self._reader

    @property
    def writer() -> asyncio.StreamWriter:
        return self._writer

    @property
    def buffer() -> net.common.ByteBuffer:
        return self._buffer

