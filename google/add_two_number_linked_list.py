"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def add_linkedlist_reversed_values(self, l: ListNode, callback: Callable):
        while l:
            callback(l.val)
            l = l.next

    def join_stack_vals_to_int(self, l: list) -> int:
        v: int = 0
        r_counter = 1
        original_l_len = len(l)
        for i in range(original_l_len):
            v += l.pop()*10**(original_l_len-r_counter)
            r_counter += 1
        return v

    def r_linkelist_from_int(self, num: int) -> ListNode:
        head: ListNode = ListNode()
        prev = None
        c = head
        while num>=1:
            val = num%10
            num //= 10
            c.val, c.next = val, ListNode() if num>=1 else None
            c = c.next


        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None  and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1

        n1, n2 = [], []
        self.add_linkedlist_reversed_values(l1, lambda x: n1.append(x))
        self.add_linkedlist_reversed_values(l2, lambda x: n2.append(x))


        r_l1_n = self.join_stack_vals_to_int(n1)
        r_l2_n = self.join_stack_vals_to_int(n2)


        totaln = r_l1_n + r_l2_n

        sum_r_linkedlist = self.r_linkelist_from_int(totaln)
        return sum_r_linkedlist
