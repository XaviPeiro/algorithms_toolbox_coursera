from collections import deque
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # bfs
        """
        val = right or left
        res.append(val) if is_last_level_element
        """
        if not root:
            return []

        next_elements = deque()
        next_elements.append((0,root))
        res = []

        candidate: tuple[Optional[int], Optional[int]] = (0, None)

        while next_elements:
            
            lvl, element = next_elements.popleft()
            if candidate[0] == lvl and element.val is not None:
                candidate = (lvl, element.val) 
            elif candidate[0] < lvl:
                to_add = None
                to_add = candidate[1]
                if to_add is not None:
                    res.append(to_add)

                candidate = (lvl, element.val)

            if element.left is not None:
                next_elements.append((lvl+1, element.left))

            if element.right is not None:
                next_elements.append((lvl+1, element.right))
        
        if candidate[1] is not None:
            res.append(candidate[1])
        return res
                
