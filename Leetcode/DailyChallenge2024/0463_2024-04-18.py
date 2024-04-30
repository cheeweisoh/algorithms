class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        ans = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    ans += 4
                
                    for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        if x + dx in range(len(grid)) and y + dy in range(len(grid[0])) and grid[x + dx][y + dy] == 1:
                            ans -= 1
        
        return ans
    

soln = Solution()
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(soln.islandPerimeter(grid))