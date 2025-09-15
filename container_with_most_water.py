"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

class Solution:
    def __call__(self, height: list[int]) -> int:
        # goal = max -> min_height + distance, min -> min_height + distance

        l,r = 0,len(height)
        res = 0
        while abs(l-r) > 1:
            
        


s = Solution()
assert s(height=[1,8,6,2,5,4,8,3,7]) == 49, s(height=[1,8,6,2,5,4,8,3,7])
assert s(height=[1,,6,2,5,4,8,15,7]) == 49, s(height=[1,8,6,2,5,4,8,3,7])
assert s(height=[1,8,3,3,3,9,1,1,1,7]) ==  56, s(height=[1,8,3,3,3,9,1,1,1,9])
assert s(height=[1,80,75,70,65,60,55,50,1,7]) ==  350, s(height=[1,8,3,3,3,9,1,1,1,9])

