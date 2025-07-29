class A:
    def __init__(self) -> None:
        self.v: bool = True
    
    def c(self):
        return lambda: self.v is True


a = A() 
f = lambda: a.v is True
print(f())
a.v= False
print(f())
print(a.c()())