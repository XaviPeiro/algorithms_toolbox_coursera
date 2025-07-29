from copy import copy
from math import factorial
from typing import List, Optional


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def get_n_perms(nums: list[int], nums_k: int) -> list[list[int]]:
            if len(nums) == 1:
                return [nums]

            res = []
            prefix = nums.pop(nums_k)

            for k, n in enumerate(nums):
                sub_res = get_n_perms(nums=copy(nums), nums_k=k)
                for sub_res_element in sub_res:
                    res.append([prefix]+sub_res_element)  # n
            return res

        for k, n in enumerate(nums):
            sub_res = get_n_perms(nums=copy(nums), nums_k=k)
            res += sub_res
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub_sol = []

        def recur():
            if len(res) == factorial(len(nums)):
                return

            if len(sub_sol) == len(nums):
                res.append(sub_sol[:])
                return

            for n in nums: # -> n^n
                if n not in sub_sol: # sum_i_1_n => !n/!(n-i) * i -> !n^2
                    sub_sol.append(n)
                    recur()
                    sub_sol.pop()
        recur()
        if not res[-1]:
            return res[-1]
        else:
            return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        prefix = []

        def recur(nums2: List[int], item_key: int, prefix: Optional[List[int]] = None):
            cv = nums2.pop(item_key)

            if prefix is None:
                prefix = list()

            if len(nums2) == 1:
                prefix.append(nums2[0])
                res.append(copy(prefix))
                prefix.pop()
                return

            # prefix.append(cv)
            for k, n in enumerate(nums2):
                prefix.append(n)
                recur(nums2=copy(nums2), item_key=k, prefix=prefix)
                prefix.pop()
            # prefix.pop()

        for k, n in enumerate(nums):
            prefix.append(n)
            recur(nums2=copy(nums), item_key=k, prefix=prefix)
            prefix.pop()

        print(res)
        return res

"""
    n*(n-1)*... = !n
    n*(n-1)
    
    Alg analysis:
         n*(1)
         n*(!(n-1)*!(n-2))
         !n*!(n-2) 
"""

if __name__ == '__main__':
    s = Solution()
    assert s.permute(nums=[1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    # assert s.permute(nums=[5,4,6,2]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
