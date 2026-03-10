# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # 1) Interleave copied nodes with original nodes
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        # 2) Assign random pointers for the copied nodes
        curr = head
        while curr:
            copy = curr.next
            if curr.random:
                copy.random = curr.random.next
            curr = copy.next

        # 3) Separate the interleaved list into original and copied lists
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next              # restore original
            copy.next = copy.next.next if copy.next else None  # link copy list
            curr = curr.next

        return copy_head
