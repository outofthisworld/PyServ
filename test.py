from world import IntervalWorldTask
from time import sleep


i = IntervalWorldTask.fromCallable(lambda: print('poll'), delay=0)

while True:
    if not i.done():
        i.poll()
        sleep(1)
    else:
        break
    
print('done')