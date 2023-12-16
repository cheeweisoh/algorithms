import collections

class Solution:
    def minTime(self, n: int, edges: list, hasApple: list) -> int:
        """Minimum Time to Collect All Apples in a Tree

        Args:
            n (int): number of vertices in tree
            edges (list): edges of the tree, where edge[i] = [a_i, b_i] means there is an edge connecting vertices a_i and b_i
            hasApple (list): true if vertex i has an apple, false otherwise

        Returns:
            count (int): minimum time in seconds spent to collect all apples in the tree
        """
        graph = collections.defaultdict(list)
        visited = [0 for i in range(n)]
        count = 0
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        def dfs(node):
            nonlocal count
            apple = hasApple[node]
            visited[node] = 1
            
            for i in graph[node]:
                if not visited[i]:
                    if dfs(i):
                        count += 2
                        apple = True
            return apple
        
        dfs(0)
        return count