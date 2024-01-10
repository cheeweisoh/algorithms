import collections

class Solution:
    def amountOfTime(self, root: TreeNode, start: int) -> int:
        adj = collections.defaultdict(set)
        self.convert(root, 0, adj)
        q = collections.deque()
        q.append(start)
        ans = 0
        visited = set()
        visited.add(start)
        
        while q:
            ls = len(q)
            while ls > 0:
                curr = q.popleft()
                
                for num in adj[curr]:
                    if num not in visited:
                        visited.add(num)
                        q.append(num)
                ls -= 1
            ans += 1
        return ans - 1
                
        
    def convert(self, node, parent, adj):
        if not node:
            return
        
        if node.val not in adj:
            adj[node.val] = set()
            adj_list = adj[node.val]
            
        if parent != 0:
            adj_list.add(parent)
        
        if node.left:
            adj_list.add(node.left.val)
        if node.right:
            adj_list.add(node.right.val)
        
        self.convert(node.left, node.val, adj)
        self.convert(node.right, node.val, adj)