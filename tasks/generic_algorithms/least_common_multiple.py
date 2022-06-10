def gcd(a, b) -> int:
    if b == 0:
        return int(a)

    remain = a % b
    return gcd(b, remain)


def least_common_multiple(a, b) -> int:
    g = gcd(a, b)
    return a*b//g


a, b = map(lambda x: int(x), input().split())

res = least_common_multiple(a, b)
print(res)
