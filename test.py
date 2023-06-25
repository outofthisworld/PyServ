from world import IntervalWorldTask
from time import sleep

i = IntervalWorldTask(2, 5)
i.fromCallable(lambda: print('poll'))

while True:
    if not i.done():
        i.poll()
        sleep(1)
    else:
        break
    
print('done')