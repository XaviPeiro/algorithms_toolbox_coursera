from typing import overload


class A:
    @overload
    def __init__(self, a: int):
        ...

    @overload
    def __init__(self, a: str):
        ...
    
    def __init__(self, a):
        self.a =a 
        

a = A(1)
b = A("s")

print(a)
print(b)
b = A(1.1)