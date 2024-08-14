# Your task is to complete this function
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:

    #Function to rotate a linked list.
    def rotate(self, head, k):
        tail = head
        lenght = 1

        while tail.next:
            lenght += 1
            tail = tail.next

        k = k % lenght
        if k == 0:
            return head
        current = head
        for _ in range(k - 1):
            current = current.next

        newh = current.next
        current.next = None

        tail.next = head
        return newh
        # code here
