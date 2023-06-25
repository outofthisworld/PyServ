import inspect
from typing import Callable

class EventEmitter(object):
    """EventEmitter"""
    def __init__(self):
        """Init"""
        self._subscribers = {}

    def subscribe(self, event: str, handler: Callable):
        """Subcribe"""
        self._subscribers.setdefault(event, []).append(handler)
    
    def subscribe_class(self, subscriber):
        def member_predicate(member): return (
            inspect.ismethod(member) or inspect.isfunction(member)
        ) and hasattr(member, "_is_event_handler") and member._is_event_handler and hasattr(member, "_event_key")

        resolved_members = inspect.getmembers(
            subscriber, predicate=member_predicate)

        members = [
            (method._event_key, method)
            for name, method in resolved_members
            if name != "__init__"
        ]
        
        for event_key, method in members:
            self._subscribers.setdefault(event_key, []).append(method)
    
    def unsubscribe(self, event:str):
        self._subscribers.pop(event)

    def unsubscribe(self, event: str, handler: Callable):
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
