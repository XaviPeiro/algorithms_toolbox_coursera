from math import sqrt, floor
from typing import List


def calculate_total_to_discrete_levels(total: int) -> int:
    return floor(-.5 + sqrt(.25+2*total))


def calculate_from_discrete_level_to_total(levels: int) -> int:
    return int(levels * (levels/2 + .5))


def maximum_number_of_prizes(total: int) -> List:
    n_of_prizes = calculate_total_to_discrete_levels(total=total)
    list_of_prizes = list(range(n_of_prizes, 0, -1))[::-1]
    list_of_prizes[-1] += total - calculate_from_discrete_level_to_total(levels=n_of_prizes)
    return list_of_prizes


if __name__ == "__main__":
    total = int(input())
    prizes: List = maximum_number_of_prizes(total=total)
    print(len(prizes))
    print(" ".join(str(prize) for prize in prizes))
