class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> [TreeNode]:
        def postorder(root, target):
            if root is None:
                return None

            root.left = postorder(root.left, target)
            root.right = postorder(root.right, target)

            if root.left == root.right and root.val == target:
                return None

            return root

        return postorder(root, target)
