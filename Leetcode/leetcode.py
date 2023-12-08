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

soln = Solution()
root1 = createTree([1,2,3,4], 0)
root2 = createTree([1,2,3,None,4], 0)
print(soln.tree2str(root1))
print(soln.tree2str(root2))
