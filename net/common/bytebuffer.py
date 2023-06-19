import typing
import struct
from . import consts


T: typing.Type = typing.TypeVar('T')
Byte = int
Short = int


class ByteBuffer(object):
    """
        ByteBuffer
    """

    def __init__(self, buffer: bytearray = bytearray(), endianess: consts.Endianess = consts.Endianess.LITTLE, **kwargs):
        self._buffer = buffer
        self._endianess: consts.Endianess = endianess
        self._index = kwargs.get('index', 0)
        

    # methods
    def read_short(self, signage: consts.SignType) -> Short:
        return self.read(consts.DataType.SHORT, signage)

    def read_int(self, signage: consts.SignType) -> int:
        return self.read(consts.DataType.INT, signage)

    def read(self, datatype: consts.DataType, signage: consts.SignType) -> typing.Type[T]:
        return self._unpack(datatype, signage)

    def read_byte(self) -> Byte:
        if self._index >= len(self.buffer):
            raise IndexError(f"Buffer out of range, no bytes to read {self.position}")

        next_byte = self.position + 1

        [byte] = self.buffer[self.position:next_byte]
        self._index = next_byte
        return byte

    def compact(self) -> 'ByteBuffer':
        self._buffer = self.buffer[self.position:]
        self.rewind()
        return self

    def chunk(self, num_bytes=0, compact=True) -> 'ByteBuffer':
        seek = self.position + num_bytes
        copy = self.buffer[self.position:seek]
        self._index = seek
        if compact:
            self.compact()
        return ByteBuffer(copy, self.endianess)
        
    def rewind(self) -> 'ByteBuffer':
        self._index = 0
        return self

    def clear(self) -> 'ByteBuffer':
        self.rewind()
        self.buffer.clear()
        return self

    def read_bytes(self, amount) -> typing.List[Byte]:
        return [self.read_byte() for i in range(amount)]

    def add_bytes(self, b) -> 'ByteBuffer':
        self.buffer.extend(b)
        return self

    def copy(self) -> 'ByteBuffer':
        return ByteBuffer(self.buffer[:], endianess=self.endianess, index=self.position)
    
    def __len__(self):
        return len(self.buffer)

    def __get_item__(self, *args, **kwargs):
        return self.buffer.__get_item__(*args, **kwargs)
    
    def __iter__(self):
        return iter(self.buffer)

    # private methods
    def _unpack(self, datatype: consts.DataType, signage: consts.SignType) -> typing.Type[T]:
        data = self.read_bytes(datatype.num_bytes)
        prefix = '<' if self.endianess == consts.Endianess.LITTLE else '>'
        with_signage = datatype.fmt_signed if signage.SIGNED else datatype.fmt_unsigned
        (out,) = struct.unpack(f"{prefix}{with_signage}",
                               bytes(data))
        return out

    # properties
    @property
    def position(self) -> int:
        return self._index
    
    @property
    def buffer(self) -> bytearray:
        return self._buffer

    @property
    def endianess(self) -> str:
        return self._endianess

    @endianess.setter
    def endianess(self, value) -> None:
        if not value in consts.Endianess:
            raise ValueError("Invalid endianess provided")

        self._endianess = value
