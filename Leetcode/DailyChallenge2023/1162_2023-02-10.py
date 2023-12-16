import collections

class Solution:
    def maxDistance(self, grid: list) -> int:
        """As Far from Land as Possible

        Args:
            grid (list): grid containing 0 and 1, where 0 represents water and 1 represents land

        Returns:
            int: maximum distance of a water cell from the nearest land cell, -1 if no land or water cells exist
        """
        n = len(grid)
        dist = 0
        q = collections.deque()
        move = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))

        if len(q) == n*n:
            return -1

        while q:
            size = len(q)
            dist += 1

            for _ in range(size):
                r, c = q.popleft()

                for dr, dc in move:
                    nrow, ncol = r + dr, c + dc

                    if 0 <= nrow < n and 0 <= ncol < n and grid[nrow][ncol] == 0:
                        grid[nrow][ncol] = 1
                        q.append((nrow, ncol))

        return dist - 1