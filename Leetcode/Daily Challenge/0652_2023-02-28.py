class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """Definition for a binary tree node
        """
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> list:
        """Find Duplicate Subtrees

        Args:
            root (TreeNode): root of a binary tree

        Returns:
            res (list): all root node of duplicate subtrees
        """
        res = []
        hmap = {}
        
        def recurse(node, path):
            if node is None:
                return '#'
            
            path += ','.join([str(node.val), recurse(node.left, path), recurse(node.right, path)])
            
            if path in hmap:
                hmap[path] += 1
                if hmap[path] == 2:
                    res.append(node)
            else:
                hmap[path] = 1
                
            
            return path
        
        recurse(root, '')
        return res