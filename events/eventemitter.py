import typing

class EventEmitter(object):
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event: str, handler: typing.Callable):
        self._subscribers.setdefault(event, []).append(handler)

    def unsubscribe(self, event: str, handler: typing.Callable):
        if (subscribers := self._subscribers.get(event)) is not None:
            subscribers.remove(handler)

    def emit(self, event: str, *args, **kwargs):
        subscribers = self._subscribers.get(event)
        if subscribers is None:
            return

        for subscriber in subscribers:
            if callable(subscriber):
                subscriber(*args, **kwargs)
