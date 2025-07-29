"""
Divide and conquer approach
"""
from hamcrest import assert_that, equal_to


def merge(nums: list, nums1: list):
    """
    :param nums: ordered list of numbers
    :param nums1: ordered list of numbers
    :return:
    """
    total_items = len(nums) + len(nums1)
    nums1.append(float("inf"))
    nums.append(float("inf"))
    n_l = []
    for i in range(total_items):
        if nums1[0] <= nums[0]:
            n_l.append(nums1.pop(0))
        else:
            n_l.append(nums.pop(0))
    return n_l

l: list
# l.pop()
# """
#     Could be faster if replaced/reordered in place
def merge_sort(nums: list) -> list:
    if len(nums) > 1:
        l = merge_sort(nums[:len(nums) // 2])
        r = merge_sort(nums[len(nums) // 2:])
        res = merge(l, r)
    else:
        if len(nums) == 1:
            res = [nums[0]]
        elif len(nums) == 0:
            res = []
        else:
            raise Exception("No fucking sense")

    return res
# def merge_sort(nums: list, nums1: list):
#     merged = nums + nums1
#     merged_len = len(merged)
#
#     if merged_len > 1:


if __name__ == "__main__":
    assert_that(merge([1, 2, 3], [4, 5, 6]), equal_to([1, 2, 3, 4, 5, 6]))
    assert_that(merge([1, 3, 6], [2, 4, 5]), equal_to([1, 2, 3, 4, 5, 6]))
    assert_that(merge([31, 41, 59,], [26, 41, 58]), equal_to([26, 31, 41, 41, 58, 59]))

    assert_that(merge_sort([1, 2, 3, 4, 5, 6]), equal_to([1, 2, 3, 4, 5, 6]))
    assert_that(merge_sort([1, 2, 6, 4, 3, 5]), equal_to([1, 2, 3, 4, 5, 6]))
    assert_that(merge_sort([31, 41, 59, 41, 58, 26]), equal_to([26, 31, 41, 41, 58, 59]))
    print("Success!")

