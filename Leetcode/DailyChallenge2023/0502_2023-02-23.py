import heapq

class T:
    def __init__(self, pro, cap):
        self.pro = pro
        self.cap = cap
        
    def __lt__(self, other):
        return self.cap < other.cap

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list, capital: list) -> int:
        """IPO

        Args:
            k (int): number of distinct projects that can be completed
            w (int): initial capital
            profits (list): profits[i] is the profit of the i-th project
            capital (list): capital[i] is the minimum capital required to start the i-th project

        Returns:
            int: final maximised capital from at most k distinct projects
        """
        minHeap = []
        maxHeap = []

        for i in range(len(capital)):
            heapq.heappush(minHeap, T(profits[i], capital[i]))

        while k > 0:
            while minHeap and minHeap[0].cap <= w:
                t = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, (-t.pro, t.cap))
            if not maxHeap:
                break
            p, c = heapq.heappop(maxHeap)
            w -= p
            k -= 1

        return w