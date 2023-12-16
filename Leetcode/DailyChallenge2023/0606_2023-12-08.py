class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addtostr(self, node: TreeNode, ans: str) -> str:
        subans = ''
        if (node.left):
            print(node.left.val)
            subans += '(' + str(node.left.val)
            subans = self.addtostr(node.left, subans)
            subans += ')'
        elif (node.right):
            subans += '()'
        
        if (node.right):
            print(node.right.val)
            subans += '(' + str(node.right.val)
            subans = self.addtostr(node.right, subans)
            subans += ')'
        
        return ans + subans
    
    def tree2str(self, root: TreeNode) -> str:
        ans = self.addtostr(root, str(root.val))
        ans = ans.replace('None', '')
        return ans