import collections

class Solution:
    def countSubTrees(self, n: int, edges: list, labels:str) -> list:
        """Number of Nodes in the Sub-Tree With the Same Label

        Args:
            n (int): number of vertices in tree
            edges (list): edges of the tree, where edge[i] = [a_i, b_i] means there is an edge connecting vertices a_i and b_i
            labels (str): labels of vertices, where labels[i] is the label for the i-th vertex

        Returns:
            ans (list): list of counts, where ans[i] is the number of vertices in the subtree of vertex i which have the same label as vertex i
        """
        graph = collections.defaultdict(list)
        ans = [0] * n
        edges.sort(reverse=True)
        
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node, parent):
            nonlocal ans
            
            count = collections.Counter()
            for child in graph[node]:
                if child != parent:
                    count += dfs(child, node)
                
            count[labels[node]] += 1
            ans[node] = count[labels[node]]
            
            return count
        
        dfs(0, -1)
        return ans