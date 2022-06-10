def gcd(a, b) -> int:
    if b == 0:
        return a

    remain = a % b
    return gcd(b, remain)

a, b = map(lambda x: int(x), input().split(" "))
res = gcd(a, b)
print(res)

