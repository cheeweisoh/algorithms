import collections
import math
import random
import heapq
import string

class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def createTree(nodeList, index):
    root = TreeNode(nodeList[index])
    
    if 2 * index + 1 < len(nodeList):
        root.left = createTree(nodeList, 2 * index + 1)
    if 2 * index + 2 < len(nodeList):
        root.right = createTree(nodeList, 2 * index + 2)
        
    return root

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        ans = []
        
        def dfs(node):
            if node:
                dfs(node.left)
                ans.append(node.val)
                dfs(node.right)
        
        dfs(root)
        return ans

soln = Solution()
root1 = createTree([1,None,2,3], 0)
root2 = createTree([1], 0)
print(soln.inorderTraversal(root1))
print(soln.inorderTraversal(root2))
