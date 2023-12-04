class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list:
        """Binary Tree Zigzag Level Order Traversal

        Args:
            root (TreeNode): root node of a binary tree

        Returns:
            ans (list): zigzag level order traversal of binary tree's node values
        """
        ans = []
        curr = [root] if root else []
        level = 0
        
        while curr:
            nums = []
            next = []
            
            for node in curr:
                nums.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
                
            if level % 2:
                nums = nums[::-1]
                
            ans.append(nums)
            level += 1
            curr = next
        
        return ans