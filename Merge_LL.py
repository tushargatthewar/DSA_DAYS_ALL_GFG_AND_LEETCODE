#User function Template for python3
'''
    Function to merge two sorted lists in one
    using constant space.

    Function Arguments: head_a and head_b (head reference of both the sorted lists)
    Return Type: head of the obtained list after merger.

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }

'''


class Solution:
    #Function to merge two sorted linked list.
    def sortedMerge(self, head1, head2):

        newnode = Node(0)
        last = newnode
        current1 = head1
        current2 = head2

        while current1 and current2:
            if current1.data < current2.data:
                last.next = current1
                current1 = current1.next
            else:
                last.next = current2
                current2 = current2.next
            last = last.next

        if current1:
            last.next = current1
        if current2:
            last.next = current2

        return newnode.next

        # code here
