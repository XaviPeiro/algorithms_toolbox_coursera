from typing import Optional


class ListNode:

    @classmethod
    def create(cls, l: list):
        head = cls(val=l[0])
        prev = head
        for k,v in enumerate(l[1:]):
            prev.next = cls(val=v)
            prev = prev.next
        return head

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = []
        node = self
        while node is not None:
            res.append(node.val)
            node = node.next
        return str(res)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curr_node = head.next
        prev_node = None
        while head is not None:
            # take curr.next
            next_node = head.next
            # reverse link
            head.next = prev_node
            prev_node = head
            head = next_node

        return head


if __name__ == "__main__":
    # test creation
    l = ListNode.create([1,2,3,4,5])
    print(l)
    # assert l == [1,2,3,4,5]
    k = Solution().reverseList(l)
    print(k)
