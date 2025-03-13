from . import t


# https://leetcode.com/problems/reverse-linked-list/

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: t.Optional[ListNode]) -> t.Optional[ListNode]:
        node = None

        while head:
            tmp = head.next
            head.next = node
            node, head = head, tmp

        return node
