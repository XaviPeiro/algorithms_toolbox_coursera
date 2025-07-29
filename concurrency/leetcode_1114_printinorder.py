from threading import Condition, Thread
from typing import Callable

class Foo:
    def __init__(self):
        self.condition = Condition()
        self.has_first: bool = False
        self.has_second: bool = False
        self.has_3rd: bool = False
    
    def _can(self, who: int) -> bool:
        all__p = [self.has_first, self.has_second, self.has_3rd] 
        can: bool = False
        print(all__p)
        if who == 1:
            return not any(all__p) # all false
        if who == 2:
            return all__p == [True, False, False]
        if who == 3:
            return all__p == [True, True, False]
        

    def first(self, printFirst: 'Callable[[], None]') -> None:
        with self.condition:
            # printFirst() outputs "first". Do not change or remove this line.
            while not self._can(1):
                print(1)
                self.condition.wait()
            printFirst()
            self.condition.notify(3)
        self.has_first = True

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.condition:        
            # printSecond() outputs "second". Do not change or remove this line.
            while not self._can(2):
                print(2)
                self.condition.wait(3)
            printSecond()
            self.condition.notify()

        self.has_second = True

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.condition:        
            # printThird() outputs "third". Do not change or remove this line.
            # self.condition.wait_for(lambda: self._can(3))
            while not self._can(3):
                print(3)
                self.condition.wait()
            printThird()
            self.condition.notify(3)

        self.has_first = False
        self.has_second = False
        self.has_3rd = False


if __name__ == "__main__":
    p = Foo()
    f = lambda: print("first")
    s = lambda: print("second")
    th = lambda: print("third")
    ll = [
        [
            Thread(target=p.first, args=[f]), 
            Thread(target=p.second, args=[s]), 
            Thread(target=p.third, args=[th])
            ],
        [
            Thread(target=p.second, args=[s]), 
            Thread(target=p.third, args=[th]),
            Thread(target=p.first, args=[f]), 
        ],        
        [
            Thread(target=p.third, args=[th]),
            Thread(target=p.second, args=[s]), 
            Thread(target=p.first, args=[f]), 
        ],
    ]
    
    for l in ll:
        print("\n\n\n")
        print("-----")
        for t in l:
            t.start()
        
        for t in l:
            t.join()

            