from math import log2, floor


def decimal_to_binary(x: int):
    res = 0
    while x>0:
        if x == 1:
            x-=1
            res += 1
        res += 10**floor(log2(x))
        x -= 2**floor(log2(x))
    return res


if __name__ == '__main__':
    print(decimal_to_binary(114))
