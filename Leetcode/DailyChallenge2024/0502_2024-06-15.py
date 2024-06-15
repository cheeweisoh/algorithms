import heapq


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: list[int], capital: list[int]
    ) -> int:
        projects = [(capital[i], profits[i]) for i in range(len(profits))]
        projects.sort()
        order = []
        i = 0

        for _ in range(k):
            # push every project that is do-able into maxheap
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(order, -projects[i][1])
                i += 1

            # if there are no available projects, break
            if not order:
                break

            # out of all possible projects, do the one with the most profit
            w -= heapq.heappop(order)

        return w
