from threading import Semaphore, Thread, Lock, Condition

import time

s = Semaphore(value=22)

print(f" initial: semaphore {s}")
def take():
    s.acquire()
    print(f"semaphore {s}")
    
    
def free():
    s.release()
    print(f"semaphore {s}")

    
    
if __name__ == "__main__":
    t1 = Thread(target=take)
    t2 = Thread(target=free)
    ts = [Thread(target=take), Thread(target=free), t1, t2]
    for i in ts:
        i.start()
    
    for i in ts:
        i.join()