#User function Template for python3
from collections import deque, defaultdict


class Solution:

    def shortestPath(self, edges, n, m, src):
        graph = defaultdict(list)

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        path = [float('inf')] * n
        path[src] = 0

        queue = deque([src])

        while queue:
            node = queue.popleft()

            for neighbour in graph[node]:
                if path[neighbour] == float('inf'):
                    path[neighbour] = path[node] + 1
                    queue.append(neighbour)

        for i in range(n):
            if path[i] == float('inf'):
                path[i] = -1

        return path

        # code here
