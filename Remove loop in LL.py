'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''


class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes

        if head is None or head.next is None:
            return

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if slow == fast:
            slow = head
            if slow == fast:
                while fast.next != slow:
                    fast = fast.next

            else:
                while slow.next != fast.next:
                    slow = slow.next
                    fast = fast.next

            fast.next = None
