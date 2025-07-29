from math import ceil
from typing import List


def maximum_salary(list_of_int: List[int]) -> int:
    """
    It finds the max digit according to a list of natural numbers.
    Natural numbers can have more than one digit.
    """
    # char_list_of_n = sorted(
    #     list(
    #         map(str, list_of_int)
    #     ),
    #     reverse=True
    # )
    # dict_char_list = dict(enumerate(char_list_of_n))
    # max_len = len(str(max(list_of_int)))
    # for key, value in dict_char_list.items():
    #     if len(value) < max_len:
    #         dict_char_list[key] = (value * ceil(max_len / len(value)))[:max_len]
    #
    # dict_char_list = dict(
    #     sorted(
    #         dict_char_list.items(),
    #         key=lambda entry: entry[1],
    #         reverse=True
    #     )
    # )
    # return int("".join(list(map(lambda x: char_list_of_n[x[0]], dict_char_list.items()))))
    # # r = sorted(list_of_int, key=cmp_to_key(lambda i, j: -2 if str(j) + str(i) < str(i) + str(j) else 0))
    # # return int("".join(map(str, r)))
    return maximum_salary2(list_of_int=list_of_int)


def approach2(list_of_int: List[int]):
    """
        bigger=> n or n1
        len_number = floor(log10(n))+1
        bn -> bigger number, sn -> smallest number
        bigger_number_part to compare = (bn_lennumber - (bn_lennumber % 10^(bn_lennumber - sm_lennumber))) / (bn_lennumber - sm_lennumber)
        bigger_number_part to compare v2 = int(bn_lennumber / 10^(bn_lennumber - sm_lennumber) )
        :return:
     """

    return


def maximum_salary2(list_of_int: List[int]):

    biggest_value = max(list_of_int)
    bvl = len(str(biggest_value))

    str_list_of_int = list(map(str, list_of_int))


    shifted_list = list(
        map(
            lambda x: x + (x * ceil( (bvl-len(x))/len(x) ))[:bvl-len(x)],
            str_list_of_int
        )
    )
    od = dict(
        sorted(
            dict(zip(range(len(shifted_list)), shifted_list)).items(),
            reverse=True,
            key=lambda x: x[1]
        )
    )
    res = ""
    for index, value in od.items():
        # print(index)
        res += str_list_of_int[int(index)]

    return int(res)

    # ordered_dict = dict(sorted(dict(zip(shifted_list, list_of_int)).items(), reverse=True))
    # res = int("".join(map(str, list(ordered_dict.values()))))
    # return res

    # for i in shifted_list:

    # coins = [10, 5, 1]
    # n_of_coins = 0
    # remaining = int(n)
    # for coin in coins:
    #     n_of_coins += remaining//coin
    #     remaining = remaining % coin
    #
    #     if remaining == 0:
    #         break
    #
    # assert remaining == 0
    # return n_of_coins


if __name__ == "__main__":
    n_numbers = int(input())
    numbers_list = list(map(int, input().split()))
    max_salary = maximum_salary(list_of_int=numbers_list)
    print(max_salary)
