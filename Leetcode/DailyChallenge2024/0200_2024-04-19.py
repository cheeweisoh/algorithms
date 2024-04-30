class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        ans = 0
        
        def dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != '1':
                return
            grid[x][y] = '0'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == '1':
                    print(i, j)
                    ans += 1
                    dfs(i, j)
        
        return ans