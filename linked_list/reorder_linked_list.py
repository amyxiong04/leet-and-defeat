class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode):
        if not head or not head.next:
            return
        
        # step 1: find middle
        slow, fast = head, head 
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # step 2: reverse second half
        prev = None
        curr = slow.next
        slow.next = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # step 3: merge two halves
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1 

            first = temp1
            second = temp2 


def createLinkedList(nums):
    dummy = ListNode(0)
    current = dummy

    for num in nums:
        current.next = ListNode(num)
        current = current.next 
    
    return dummy.next

def printLinkedList(linkedlist):
    curr = linkedlist
    while curr:
        print(curr.val)
        curr = curr.next



solution = Solution()

list = [1, 2, 3, 4, 5, 6]
linkedlist = createLinkedList(list)
printLinkedList(linkedlist)
solution.reorderList(linkedlist)
printLinkedList(linkedlist)
