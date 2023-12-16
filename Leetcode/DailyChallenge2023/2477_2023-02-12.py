import collections

class Solution:
    def __init__(self):
        self.ans = 0
    
    def dfs(self, node: int, seats: int, visited: list, road_map: dict):
        visited[node] = 1
        count = 1
        
        for nb in road_map[node]:
            if not visited[nb]:
                count += self.dfs(nb, seats, visited, road_map)
                
        x = count // seats
        if count % seats:
            x += 1
        if node != 0:
            self.ans += x
        
        return count
    
    def minimumFuelCost(self, roads: list, seats: int) -> int:
        road_map = collections.defaultdict(list)
        for x,y in roads:
            road_map[x].append(y)
            road_map[y].append(x)
        
        visited = [0] * (len(roads) + 1)
        
        self.dfs(0, seats, visited, road_map)
        
        return self.ans
