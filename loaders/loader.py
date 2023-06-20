"""
    Loader
"""
import abc
import typing

T = typing.TypeVar('T')


class Loader(abc.ABC):
    """
        Loader
    """
    @abc.abstractmethod
    def load(self, *args, **kwargs) -> T:
        """
            Load the thing
        """
