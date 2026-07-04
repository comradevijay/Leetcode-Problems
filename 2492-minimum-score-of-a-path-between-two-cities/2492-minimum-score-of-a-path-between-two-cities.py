class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))

        visited = [False] * (n + 1)
        ans = float('inf')
        stack = [1]
        visited[1] = True
        while stack:
            u = stack.pop()
            for v, w in adj[u]:
                ans = min(ans, w)
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna