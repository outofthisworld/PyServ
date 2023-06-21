import typing

class EventEmitter(object):
    """EventEmitter"""
    def __init__(self):
        """Init"""
        self._subscribers = {}

    def subscribe(self, event: str, handler: typing.Callable):
        """Subcribe"""
        self._subscribers.setdefault(event, []).append(handler)

    def unsubscribe(self, event: str, handler: typing.Callable):
        """Ubsubscribe"""
        if (subscribers := self._subscribers.get(event)) is not None:
            subscribers.remove(handler)

    def emit(self, event: str, *args, **kwargs):
        """Emit"""
        subscribers = self._subscribers.get(event)
        if subscribers is None:
            return

        for subscriber in subscribers:
            if callable(subscriber):
                subscriber(*args, **kwargs)
