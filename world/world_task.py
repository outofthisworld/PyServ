import typing
from typing import Optional

class WorldTask:
    def __init__(self):
        self._task = None

    @classmethod
    def fromCallable(cls, task: typing.Callable) -> 'WorldTask':
        if not callable(task):
            raise ValueError("Must be a callable task")
        
        instance = cls()
        instance._task = task
        return instance

    def __call__(self) -> None:
        self.poll()

    def poll(self) -> None:
        if callable(self._task):
            self._task()

    def done(self) -> bool:
        return False

    @property
    def task(self, task: typing.Callable) -> None:
        self.fromCallable(task)


class IntervalWorldTask(WorldTask):
    def __init__(self, delay: int = 0, initialDelay=False, times: Optional[int] = None):
        super().__init__()
        self._delay = max(delay, 0)
        self._times = times
        self._attempts = 0 if not initialDelay else self._delay

    def __str__(self):
        return f"IntervalWorldTask(delay={self._delay},times={self._times},attempts={self._attempts})"

    @classmethod
    def fromCallable(cls, task: typing.Callable, **kwargs) -> 'IntervalWorldTask':
        interval_task = super().fromCallable(task)
        interval_task.__init__(**kwargs)
        return interval_task

    def poll(self) -> None:
        if self._times is not None and self._times <= 0:
            return

        if self._attempts > 0:
            self._attempts = self._attempts - 1
            return

        super().poll()
        self._attempts = self._delay

        if self._times is not None:
            self._times = self._times - 1

    def done(self) -> bool:
        if self._times is not None and self._times <= 0:
            return True

        return False
