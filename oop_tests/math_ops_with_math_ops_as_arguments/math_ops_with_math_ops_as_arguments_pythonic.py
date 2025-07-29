"""
Model a solution that allows you to pass integers but operators too, e.g.:
assert Sum(1,1) == 2
assert Sum(Sum(1,1), Sum(1,1)) == 4
assert Sum(Mul(2,3), Sum(1,1)) == 12

"""


class Sum:
    def __init__(self, a, b):
        self.left = a
        self.right = b

    def __getattribute__(self, name):
        if name in ('left', 'right'):
            operand = object.__getattribute__(self, name)
            if isinstance(operand, int):
                return operand
            elif isinstance(operand, Sum):
                return operand.left + operand.right
        return object.__getattribute__(self, name)

    def __eq__(self, target):
        return self.left + self.right == target

    def __res(self):
        return self.left + self.right

    def __add__(self, target):
        return self.__res() + target.__res()

class Mul:
    def __init__(self, a, b):
        self.left = a
        self.right = b


if __name__ == '__main__':
    assert Sum(1, 1) == 2
    assert Sum(Sum(1, 1), Sum(1, 1)) == 4
    assert Sum(Sum(1, 1), Sum(1, 1)) != 5
    assert Sum(Sum(Sum(1, 1), Sum(1, 1)), Sum(Sum(1, 1), Sum(1, 1))) == 8
    assert Sum(2,44).left == 2
    assert Sum(2,44).right == 44

    assert Sum(1, 1) + Sum(1, 1) == 4
    assert Sum(1, 1) * 2 == 4
    # print(f"non-existing attr: {Sum(1,1).name}")
    # assert Sum(Mul(2, 3), Sum(1, 1)) == 12
