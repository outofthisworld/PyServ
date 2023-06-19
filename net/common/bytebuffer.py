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

    def __init__(self, buffer: bytearray = bytearray(), endianess: consts.Endianess = consts.Endianess.LITTLE):
        self._buffer = buffer
        self._endianess: consts.Endianess = endianess

    # methods
    def read_short(self, signage: consts.SignType) -> Short:
        return self.read(consts.DataType.SHORT, signage)

    def read_int(self, signage: consts.SignType) -> int:
        return self.read(consts.DataType.INT, signage)

    def read(self, datatype: consts.DataType, signage: consts.SignType) -> typing.Type[T]:
        return self._unpack(datatype, signage)

    def read_byte(self) -> byte:
        if length := len(self.buffer) < 1:
            raise IndexError(f"Buffer out of range, no bytes to read {length}")

        [byte] = self.buffer[:1]
        self._buffer = self.buffer[1:]
        return byte

    def clear(self) -> None:
        self._buffer.clear()

    def read_bytes(self, amount) -> typing.List[Byte]:
        return [self.read_byte() for i in range(amount)]

    def add_bytes(self, b) -> None:
        self.buffer.extend(b)

    def copy(self) -> 'ByteBuffer':
        return ByteBuffer(self.buffer[:], endianess=self.endianess)

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
