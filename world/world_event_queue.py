import queue


class WorldEventQueue:
    def __init__(self, **kwargs):
        self._event_queue = queue.Queue()

    def poll(self):
        while not self._event_queue.empty:
            task = self._event_queue.get(False)
            if task is not None:
                task.poll()
