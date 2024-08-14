#User function Template for python3
'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''


class Solution:

    def addOne(self, head):
        #Returns new head of linked List.
        def rev(head):
            pre = None
            current = head

            while current:
                newnode = current.next
                current.next = pre
                pre = current
                current = newnode

            return pre

        head = rev(head)

        current = head
        carry = 1

        while current and carry:
            total = current.data + carry
            carry = total // 10
            current.data = total % 10
            pre = current
            current = current.next

        if carry:
            pre.next = Node(carry)

        return rev(head)
