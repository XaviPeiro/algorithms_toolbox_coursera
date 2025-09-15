class Combination2:
    def __call__(self, n: int, k: int):
        def bt(fr: int, nel: int) -> list:
            res = []
            for i in range(fr, n+1):
                ans = []
                if nel > 1:
                    ans = bt(fr+1, nel=nel-1)
                
                for a in ans:
                    res.append(a.append(i))

                res.append(ans)
            
            return res

        return bt(fr=1, nel=k)
            

class Combination:
    def __call__(self, nums: list[int], k: int):
        res = []
        ans = []
        visited = set()

        def traceback(nums: list[int]):
            visited_in_lvl = []
            for num in nums:
                if num in visited:
                    continue

                ans.append(num)

                if len(ans) == k:
                    res.append(ans.copy())
                    ans.pop()
                    continue

                visited.add(num)
                visited_in_lvl.append(num)
                traceback(nums=nums)
                # visited.remove(num)
                
                ans.pop()
            else:
                for num in visited_in_lvl:
                    visited.remove(num)
        
        traceback(nums=nums)
        return res


class Permutation:
    def __call__(self, nums: list[int]):
        res = []
        ans = []
        visited = set()

        def traceback(nums: list[int]):
            for num in nums:
                if num in visited:
                    continue

                ans.append(num)

                if len(ans) == len(nums):
                    res.append(ans.copy())
                elif len(ans)< len(nums):
                    visited.add(num)
                    traceback(nums=nums)
                    visited.remove(num)
                
                ans.pop()
        
        traceback(nums=nums)
        return res
        
if __name__ == "__main__":
    p = Permutation()
    assert p([1,2,3]) == [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]], p([1,2,3])
    c = Combination()
    assert c([1,2,3,4,], 2) == [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

    # assert s() == ...