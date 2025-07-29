import pytest

def main(number: int) -> bool:
    is_prime: bool = False

    for n in range(1, number+1):
        if number%n == 0 and n not in (number, 1):
            break
    else:
        is_prime = True
    
    return is_prime and number not in (0, 1)


def test():
    assert main(7) is True
    assert main(199) is True
    assert main(73) is True
    assert main(1) is False
    assert main(0) is False
    assert main(4) is False
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]
    for p in primes:
        assert main(p) is True

    not_primes = [8,12,32, 177, 202, 184, 188, 192, 186, 185]
    for np in not_primes:
        assert main(np) is False
    

not_primes = [8,12,32, 177, 202, 184, 188, 192, 186, 185]
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]
@pytest.mark.parametrize("n", primes)
def test_primes(n):
    assert main(n) is True

    
@pytest.mark.parametrize("n", not_primes)
def test_not_primes(n):
    assert main(n) is False
    

if __name__ == "__main__":
    test()
    # main()