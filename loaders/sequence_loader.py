import abc
from collections.abc import Iterable,Sequence
from . import Loader

class SequenceLoader(Loader, Iterable, Sequence):
    def __init__(self):
        self._data = []

    def __iter__(self):
        return iter(self._data)
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __len__(self):
        return len(self._data)