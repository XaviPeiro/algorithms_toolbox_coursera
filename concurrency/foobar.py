from threading import Condition, Event, Thread
from typing import Callable


class FooBar:
    def __init__(self, n):
        self.n = n
        self.is_foo_time: bool = True
        self._cond = Condition()
        

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            with self._cond:
                self._cond.wait_for(lambda: self.is_foo_time is True)
                printFoo()
                self.is_foo_time = False
                self._cond.notify_all()
        # else:
        #     self._cond.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            with self._cond:
                self._cond.wait_for(lambda: self.is_foo_time is False)
                printBar()
                self.is_foo_time = True
                self._cond.notify_all()



            
if __name__ == "__main__":
    fb= FooBar(3)
    
    foo, bar = lambda: print("foo"), lambda: print("bar")
    ts = [Thread(target=fb.foo, args=[foo]), Thread(target=fb.bar, args=[bar]) ]

    for t in ts:
        t.start()

    for t in ts:
        t.join()
