import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;

class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n == 1) {
            return Collections.singletonList(0);
        }

        Map<Integer, List<Integer>> graph = new HashMap<>();
        int[] degrees = new int[n];

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            graph.computeIfAbsent(u, k -> new ArrayList<>()).add(v);
            graph.computeIfAbsent(v, k -> new ArrayList<>()).add(u);
            degrees[u]++;
            degrees[v]++;
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (degrees[i] == 1) {
                queue.offer(i);
            }
        }

        int remain = n;
        while (remain > 2) {
            int size = queue.size();
            remain -= size;

            for (int i = 0; i < size; i++) {
                int leaf = queue.poll();

                if (graph.containsKey(leaf)) {
                    for (int neighbour : graph.get(leaf)) {
                        degrees[neighbour]--;
                        if (degrees[neighbour] == 1) {
                            queue.offer(neighbour);
                        }
                    }
                }
            }
        }

        return new ArrayList<>(queue);
    }
}