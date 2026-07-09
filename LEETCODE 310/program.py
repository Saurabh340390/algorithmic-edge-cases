class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        degree = [0]*n
        adjLst = [[] for _ in range(n)]
        for u, v in edges:
            adjLst[v].append(u)
            adjLst[u].append(v)
            degree[u] += 1
            degree[v] += 1
        queue = deque()
        for node in range(n):
            if degree[node] == 1:
                queue.append(node)
        remaining = n
        while remaining > 2:
            leaf_count = len(queue)
            remaining -= leaf_count
            for _ in range(leaf_count):
                node = queue.popleft()
                for neighbor in adjLst[node]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
        return list(queue)
