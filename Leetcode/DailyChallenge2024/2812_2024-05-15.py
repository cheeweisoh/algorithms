import collections
import heapq


class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return 0

        score = [[float("inf")] * n for _ in range(n)]

        def bfs():
            q = collections.deque()

            for i in range(n):
                for j in range(n):
                    if grid[i][j]:
                        score[i][j] = 0
                        q.append((i, j))

            while q:
                x, y = q.popleft()
                s = score[x][y]

                for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < n and 0 <= ny < n and score[nx][ny] > s + 1:
                        score[nx][ny] = s + 1
                        q.append((nx, ny))

        bfs()

        vis = [[False] * n for _ in range(n)]
        pq = [(-score[0][0], 0, 0)]
        heapq.heapify(pq)

        while pq:
            safe, x, y = heapq.heappop(pq)
            safe = -safe

            if x == n - 1 and y == n - 1:
                return safe

            vis[x][y] = True

            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny]:
                    s = min(safe, score[nx][ny])
                    heapq.heappush(pq, (-s, nx, ny))
                    vis[nx][ny] = True

        return -1
