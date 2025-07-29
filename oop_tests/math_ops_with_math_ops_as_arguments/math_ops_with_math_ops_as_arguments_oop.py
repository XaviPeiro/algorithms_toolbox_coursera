"""
Model a solution that allows you to pass integers but operators too, e.g.:
assert Sum(1,1) == 2
assert Sum(Sum(1,1), Sum(1,1)) == 4
assert Sum(Mul(2,3), Sum(1,1)) == 12

"""


class Sum:
    def __init__(self, a: int, b: int) -> None:
        ...




if __name__ == '__main__':
    assert Sum(1, 1) == 2
    assert Sum(Sum(1, 1), Sum(1, 1)) == 4
    assert Sum(Sum(1, 1), Sum(1, 1)) != 5
    assert Sum(Sum(Sum(1, 1), Sum(1, 1)), Sum(Sum(1, 1), Sum(1, 1))) == 8
    assert Sum(2,44).left == 2
    assert Sum(2,44).right == 44

    assert Sum(1, 1) + Sum(1, 1) == 4