import collections
import math
import random
import heapq
import string
import bisect

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
    def rangeSumBST(self, root: TreeNode, low: int, high: int):
        ans = 0
        
        def dfs(node):
            nonlocal ans
            if not node:
                return
            else:
                if low <= node.val <= high:
                    ans += node.val
                dfs(node.left)
                dfs(node.right) 
       
        dfs(root) 
        return ans

def main():
    soln = Solution()
    node = createTree([10, 5, 15, 3, 7, None, 18], 0)
    low = 7
    high = 15
    print(soln.rangeSumBST(node, low, high))

if __name__ == "__main__":
    main()
