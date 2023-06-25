from world import IntervalWorldTask
from time import sleep


i = IntervalWorldTask.fromCallable(lambda: print('poll'), delay=2)

while True:
    if not i.done():
        i.poll()
        sleep(1)
    else:
        break
    
print('done')