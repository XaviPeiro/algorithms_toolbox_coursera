# from generic_algorithms.utils import submittable


def fibonacci_number(x: int) -> int:
    res = {}
    for i in range(x+1):
        if i <= 1:
            res[i] = i
        else:
            res[i] = res[i-1] + res[i-2]
    return res[i]

n = int(input())
print(fibonacci_number(n))
