import collections

class Solution:
    def numberOfGoodPaths(self, vals: list, edges: list) -> int:
        """Number of Good Paths

        Args:
            vals (list): 0-indexed integer array where vals[i] denotes the value of the i-th node
            edges (list): 2d integer array where edges[i] = [a_i, b_i] denotes that there is an undirected edge connecting nodes a_i and b_i

        Returns:
            res (int): number of distinct good paths
        """
        n = len(vals)
        p = list(range(n))
        count = [collections.Counter({vals[i]:1}) for i in range(n)]
        edges = sorted((max(vals[i],vals[j]),i,j) for i,j in edges)
        res = n
        
        def find(i):
            if p[i] != i:
                p[i] = find(p[i])
            return p[i]
        
        for val, i, j in edges:
            pi, pj = find(i), find(j)
            res += count[pi][val]*count[pj][val]
            p[pi] = pj
            count[pj][val] += count[pi][val]
        
        return res