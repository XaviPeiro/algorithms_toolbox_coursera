import math
from collections import deque, defaultdict
from math import log
from pprint import pprint
from queue import Queue
from typing import Self


# class Node:
#     val: int
#     next_nodes: list
#
#     def __init__(self, val: int | None = None, next_node: list[Self] | None = None):
#         self.val = val
#         self.next_nodes = next_node or []
#
#     def add_next_node(self, node: Self) -> None:
#         self.next_nodes.append(node)
#
#     @staticmethod
#     def btree_from_list(values: list[int | list]) -> Self:
#         head = Node()
#
#         pointer = head
#         while values and (value := values.pop()):
#
#             pointer.val = value
#             pointer.add_next_node((pointer := Node()))
#
#         return head
#
#     def __str__(self):
#         for node in self.next_nodes:
#             print(f"lvl {lvl}: {nums}")
#             print(f"{'-'*10}")


import random


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)


def generate_random_binary_tree(size):
    if size == 0:
        return None

    # Choose random sizes for left and right subtrees
    random.seed(19)
    left_size = random.randint(0, size - 1)
    right_size = size - 1 - left_size

    # Generate left and right subtrees recursively
    left_subtree = generate_random_binary_tree(left_size)
    right_subtree = generate_random_binary_tree(right_size)

    # Create new node with random value
    root = Node(random.randint(0, 100))

    # Assign left and right subtrees to children
    root.left = left_subtree
    root.right = right_subtree

    return root


def bfs(root: Node) -> dict:
    pending_elements: deque = deque([root])
    lvl: dict = defaultdict(list)
    counter: int = 1
    while pending_elements and (n_element := pending_elements.popleft()):

        lvl[int(log(counter,2))].append((n_element.value, n_element.left, n_element.right))
        if n_element.left:
            pending_elements.append(n_element.left)
        if n_element.right:
            pending_elements.append(n_element.right)
        counter += 2

    return dict(lvl)


def dfs(root: Node) -> dict:
    pending_elements: deque[Node] = deque([root])
    lvl: defaultdict[int, list] = defaultdict(list)
    counter: int = 1
    while pending_elements and (next_element := pending_elements.pop()):
        lvl[int(log(counter, 2))].append(next_element.value)
        if next_element.right:
            pending_elements.append(next_element.right)
        if next_element.left:
            pending_elements.append(next_element.left)

        counter += 2

    return dict(lvl)


root = generate_random_binary_tree(15)
bfs_res = bfs(root)
pprint(bfs_res)

dfs_res = dfs(root)
pprint(dfs_res)


