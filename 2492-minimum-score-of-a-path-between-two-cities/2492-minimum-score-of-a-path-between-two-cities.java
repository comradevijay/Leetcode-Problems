class Solution {
    public int minScore(int n, int[][] roads) {
        List<int[]>[] adj = new List[n + 1];
        for (int i = 1; i <= n; i++) adj[i] = new ArrayList<>();
        for (int[] r : roads) {
            adj[r[0]].add(new int[]{r[1], r[2]});
            adj[r[1]].add(new int[]{r[0], r[2]});
        }

        boolean[] visited = new boolean[n + 1];
        int ans = Integer.MAX_VALUE;
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(1);
        visited[1] = true;
        while (!stack.isEmpty()) {
            int u = stack.pop();
            for (int[] edge : adj[u]) {
                int v = edge[0], w = edge[1];
                ans = Math.min(ans, w);
                if (!visited[v]) {
                    visited[v] = true;
                    stack.push(v);
                }
            }
        }
        return ans;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna