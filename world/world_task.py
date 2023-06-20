import typing

class WorldTask:
    def __init__(self):
        self._task = None

    def fromCallable(self, task: typing.Callable) -> 'WorldTask':
        self._task = task

    def __call__(self) -> None:
        self.poll()
    
    def poll(self) -> None:
        if callable(self._task):
            self._task()

    @property
    def task(self, task: typing.Callable) -> None:
        self.fromCallable(task)