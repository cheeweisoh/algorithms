class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        """Definition for a QuadTree node
        """
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: list) -> Node:
        """Construct Quad Tree

        Args:
            grid (list): n * n matrix of 0's and 1's

        Returns:
            Node: quad tree representation of the grid
        """
        return self.helper(grid, 0, 0, len(grid))

    def helper(self, grid, i, j, w):
        if self.allSame(grid, i, j, w):
            return Node(grid[i][j] == 1, True)

        node = Node(True, False)
        node.topLeft = self.helper(grid, i, j, w // 2)
        node.topRight = self.helper(grid, i, j + w // 2, w // 2)
        node.bottomLeft = self.helper(grid, i + w // 2, j, w // 2)
        node.bottomRight = self.helper(grid, i + w // 2, j + w // 2, w // 2)
        return node

    def allSame(self, grid, i, j, w):
        for x in range(i, i + w):
            for y in range(j, j + w):
                if grid[x][y] != grid[i][j]:
                    return False
        return True