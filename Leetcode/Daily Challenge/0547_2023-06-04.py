class Solution:
    def findCircleNum(self, isConnected: list) -> int:
        visited = [0] * len(isConnected)
        provinces = 0
        
        def dfs(city):
            visited[city] = 1
            for j in range(len(isConnected)):
                if (not visited[j]) and isConnected[city][j]:
                    dfs(j)
        
        for i in range(len(isConnected)):
            if not visited[i]:
                provinces += 1
                dfs(i)
            
        return provinces
