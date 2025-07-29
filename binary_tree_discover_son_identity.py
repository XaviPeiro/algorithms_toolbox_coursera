"""
Un padre puede siempre tiene dos hijos.
Los hijos puede ser doctores o ingenieros.
Si el padre es D el primer hijo es D y el segundo E, si el padre es E el primer hijo es E y el segundo D.
El primero de esta saga es un E.
Crea un alg que determine qué es (E o D) el nth hijo para cualquier generación .
"""
from math import log2, ceil

from hamcrest import assert_that, equal_to

"""
ED -> 2nd
sequence = ED
for each X 2 -> gen
    if X%2 == 1
        seq += [::-1]
    else seq + swapped(seq)

return seq[2**(gen-1)+child]
"""


def papa_told_me_i_am(parent: str, child: int) -> str:
    options = {"E": "D", "D": "E"}
    if child % 2 == 0:
        res = options[parent]
    else:
        res = parent

    return res


def get_profession_recursively(generation: int, child: int) -> str:
    """
        parent = gen-1 and child=ceil(child/2)
        iam = parent if child%2 == 1 else swap
    """
    parent_gen, parent_child = generation-1, ceil(child/2)
    if generation == 1:
        return "E"
    else:
        parent = get_profession_recursively(generation=parent_gen, child=parent_child)
    iam = papa_told_me_i_am(parent=parent, child=child)
    return iam


if __name__ == "__main__":
    """
            E
       /         \
      E           D
    /   \        /  \
   E     D      D    E
  / \   / \    / \   / \
 E   D D   E  D   E E   D
/ \ / \ /\  /\ /\ /\ /\  /\
ED DE DE ED DE ED ED DE
    """

    if __name__ == "__main__":
        assert_that(get_profession_recursively(generation=1, child=1), equal_to("E"))
        assert_that(get_profession_recursively(generation=2, child=1), equal_to("E"))
        assert_that(get_profession_recursively(generation=2, child=2), equal_to("D"))
        assert_that(get_profession_recursively(generation=4, child=1), equal_to("E"))
        assert_that(get_profession_recursively(generation=4, child=2), equal_to("D"))
        assert_that(get_profession_recursively(generation=4, child=5), equal_to("D"))
        assert_that(get_profession_recursively(generation=4, child=6), equal_to("E"))
        assert_that(get_profession_recursively(generation=4, child=7), equal_to("E"))
        assert_that(get_profession_recursively(generation=5, child=1), equal_to("E"))