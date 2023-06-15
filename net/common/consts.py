import enum

class SignType(enum.Enum):
    SIGNED = 0
    UNSIGNED = 1

class DataType(enum.Enum):
    SHORT = ('h', 'H', 2)
    INT = ('i', 'I', 4)
    
    def __init__(self, fmtsigned, fmtunsigned, numbytes):
        self._fmtsigned: str = fmtsigned
        self._fmtunsigned: str = fmtunsigned
        self._numbytes: int = numbytes
        
    @property
    def fmt_signed(self):
        return self._fmtsigned
    @property
    def fmt_unsigned(self):
        return self._fmtunsigned
    @property
    def num_bytes(self):
        return self._numbytes

class Endianess(enum.Enum):
    LITTLE = 'little'
    BIG = 'big'