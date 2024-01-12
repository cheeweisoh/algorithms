class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        diff = 0

        def helper(node, min_val, max_val):
            nonlocal diff
            if not node:
                return
            diff = max(diff, max(abs(min_val - node.val), abs(max_val - node.val)))
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)
            helper(node.left, min_val, max_val)
            helper(node.right, min_val, max_val)
        
        helper(root, root.val, root.val)
        return diff