from random import randint
from threading import Lock, Thread
import threading
import sys
import time
from typing import Optional, Union, cast

# def tracer(frame, event, arg):
#     if event == "line":
#         print(f"{time.time():.6f}  {threading.current_thread().name:<10} "
#               f"{frame.f_code.co_name}:{frame.f_lineno}")
#     return tracer

# sys.settrace(tracer)
# threading.settrace(tracer)

class Counter:

    def __init__(self):
        self.count = 0
        self.lock = Lock()

    def increment(self):
        for b in range(100_000_0):

            # with self.lock:
                # value = self.count

                # if b % 1000 == 0:
                    # time.sleep(0)

                # self.count = value + 1
            self.count += 1
            # print(self.count)
            # print(1)

def incr():
    global a
    for _ in range(5_0000_000):
        a += 1
    
if __name__ == "__main__":
    
    for i in range(10):
        a =0 
        # Sets the thread switch interval
        sys.setswitchinterval(1e-6)

        print(i)
        numThreads = 8
        expected_v=50_000_000 * numThreads
        threads: list[Optional[Thread]] = [None] * numThreads
        counter = Counter()

        for i in range(0, numThreads):
            # threads[i] = Thread(target=counter.increment)
            threads[i] = Thread(target=incr)

        for i in range(0, numThreads):
            cast(Thread, threads[i]).start()

        for i in range(0, numThreads):
            threads[i].join()


        # if counter.count != expected_v:
        if a != expected_v:
            print(" count = {0}".format(a), flush=True)
            break
        else:
            print(f" count = {expected_v} - Try re-running the program.")
