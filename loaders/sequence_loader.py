from collections.abc import Iterable, Sequence
from . import Loader

class SequenceLoader(Sequence, Iterable, Loader):
    """Sequence Loader"""
    def __init__(self):
        """Init"""
        super().__init__()
        self._data = []

    def __iter__(self):
        """Iter"""
        return iter(self._data)

    def __getitem__(self, index):
        """Get item"""
        return self._data[index]

    def __len__(self):
        """Len"""
        return len(self._data)

    def __contains__(self, item):
        """Contains"""
        return item in self._data
