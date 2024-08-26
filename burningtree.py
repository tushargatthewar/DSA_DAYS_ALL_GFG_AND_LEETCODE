#User function Template for python3
from collections import deque


class Solution:

    def minTime(self, root, target):
        # code here
        if not root:
            return 0

        table = {}
        targetn = None

        def check(node, parent=None):
            nonlocal targetn
            if node:
                table[node] = parent
                if node.data == target:
                    targetn = node
                check(node.left, node)
                check(node.right, node)

        check(root)

        queue = deque([targetn])
        visited = set([targetn])
        time = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                current = queue.popleft()

                if current.left and current.left not in visited:
                    visited.add(current.left)
                    queue.append(current.left)

                if current.right and current.right not in visited:
                    visited.add(current.right)
                    queue.append(current.right)

                parent = table[current]
                if parent and parent not in visited:
                    visited.add(parent)
                    queue.append(parent)

            if queue:
                time += 1

        return time
