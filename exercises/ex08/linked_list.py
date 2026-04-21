"""Linked lists.py."""

from __future__ import annotations


class Node:
    """Nodes from COMP 110!."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Contructor for Node Object."""
        self.value = value
        self.next = next


def sum(head: Node) -> int:
    """Sum nodes together."""
    # base case
    if head.next is None:
        return head.value
    # recursive rule
    else:
        return sum(head.next) + head.value
    # next nodes sum + my value


# Instantiate

node_c: Node = Node(4, None)
node_b: Node = Node(0, node_c)
node_a: Node = Node(5, node_b)

# value of node_b (remember that node_b is node_a.next)
# print(node_a.next.value)

# value of node_c (remember node_c is node_a.next.next.value)
# print(node_a.next.next.value)


def value_at(head: Node | None, index: int) -> int:
    """Returns the value of a Node stored a given index."""
    # You'll need to modify both arguments to bring recursive call closer to basecase
    # An edge case occurs when the list is empty
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    # A seocnd base case occurs when the index is 0
    if index == 0:
        return head.value
    # generating the next node so it can call for its value
    return value_at(head.next, index - 1)

    # Return the value of the current Node being processed on the list


def max(head: Node | None) -> int:
    """Returns te maximum value in the linked list."""
    max_value: int = 0
    # If the linked list is empty, raise a ValueError
    if head is None:
        raise ValueError("Cannot call max with None")
    # If the next node is None, it is automatically the max!
    if head.next is None:
        return head.value
    max_value = max(head.next)
    return head.value if head.value > max_value else max_value


def linkify(items: list[int]) -> Node | None:
    """Links values in same order as input."""
    # If the list is empty it cannot link anything
    if len(items) == 0:
        return None
    # Node(items[0], is saying pull the item (value) in this index
    # After linkify(item[1:]) will start by calling the next one by slicing
    # [1:] leaving off the ending index, defaults it to the len of the list
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Node * factor."""
    # edge case
    if head is None:
        return None
    # This is making the current value factor, however it also calls for the next node
    # This will continue until it gets to the edge case
    # Once it is none it will return it and
    # return the new list of factors

    return Node(head.value * factor, scale(head.next, factor))
