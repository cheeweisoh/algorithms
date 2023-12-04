import collections

class Solution:
    def longestPath(self, parent: list, s: str) -> int:
        """Longest Path With Different Adjacent Characters

        Args:
            parent (list): tree rooted at node 0, where parent[i] is the parent of node i
            s (str): label for each node, where str[i] is the label for node i

        Returns:
            count (int): length of longest path in the tree such that no pair of adjacent nodes on the path have the same character
        """
        graph = collections.defaultdict(list)
        count = 1
        
        for node, par in enumerate(parent):
            graph[par].append(node)
        
        def dfs(node):
            nonlocal count
            
            max1 = 0
            max2 = 0
            
            for child in graph[node]:
                child_path = dfs(child)
                
                if s[child] != s[node]:
                    if child_path > max1:
                        max1, max2 = child_path, max1
                    elif child_path > max2:
                        max2 = child_path
                        
            count = max(count, max1+max2+1)
            return max1+1
            
        dfs(0)
        return count