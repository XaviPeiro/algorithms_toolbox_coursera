from collections import defaultdict


class Solution:
    def __call__(self, v: list, target: int) -> bool:
        remaining = defaultdict(list)  # imporve: set
        [remaining[i].extend((k1, k2)) for k1, v1 in enumerate(v) for k2, v2 in enumerate(v) if
        (i := target - (v1 + v2)) >= 0 and k1 != k2]
        for kval, val in enumerate(v):
            if val in remaining:
                return True
            # remaining[target-val].append(kval)
        return False


a = tuple()
if __name__ == "__main__":
    s = Solution()
    assert s(v=[1, 3, 5, 6], target=10) == True
    assert s(v=[1, 3, 5, 6, 2], target=11) == True
    assert s(v=[1, 3, 0, 0, 2], target=11) == False
    assert s(v=[1, 3, 11, 10, 2], target=11) == False
    assert s(v=[1, 0, 11, 0, 2], target=11) == True
