import sys
from collections import deque
k = set()
a: int =2

def c(l: list):
    for i in l:
        c  = ...
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, Callable
float()
class Solution:
        def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
            sentinel = TreeNode(float('inf'))
            sentinel.right = root

            current = sentinel
            while current.right is not None and current.right.val > val:
                current = current.right

            prev_r = current.right
            current.right = TreeNode(val)
            current.right.left = prev_r
            return sentinel.right

if __name__ == "__main__":
    s = Solution()
    assert s.insertIntoMaxTree(root=[4,1,3,None,None,2], val=5) == [5,4,None,1,3,None,None,2]
    # assert s.bfs_get(root=[4,1,3,None,None,2], val=5) == [None, 4]
    # assert s.bfs_get(root=[10,7,5,None,None,2], val=4) == [5, 2]