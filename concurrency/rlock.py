from threading import RLock, Lock, Thread
import pytest

recursive_v: int = 0
def recursive(l: Lock):
    # timeout=0? blocking=False?
    l.acquire()
    global recursive_v 
    recursive_v += 1
    # l.release()
    print(recursive_v)
    if recursive_v > 10:
        return
    recursive(l)
    

# Test 
@pytest.mark.xfail
def test_recursive_w_lock():
    assert False
    assert True
    
if __name__ == "__main__":
    l = Lock()
    l = RLock()
    t = Thread(target=recursive, kwargs={"l": l})
    t.start()
    t.join()
    print(f"last {recursive_v}")

