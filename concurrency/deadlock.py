from threading import Lock, Thread, RLock
import time

d1 = RLock()
d2 = RLock()

# d1 = Lock()
# d2 = Lock()
# Globals
user = {}
credits = {} 

def one():
    d1.acquire()
    time.sleep(0)
    d2.acquire()
    global user
    global credits
    user_id = 123
    user[user_id] = "pupa"
    credits[user_id] = 0
    d1.release()
    d2.release()
    
def two():
    d2.acquire()
    time.sleep(0)
    d1.acquire()
    global credits
    credits[123] += 1
    d2.release()
    d1.release()

    
if __name__ == "__main__":
    t1 = Thread(target=one)
    t2 = Thread(target=two)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(credits)
    print(user)
