class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        currTime = customers[0][0]
        totalTime = 0
        n = len(customers)

        for a, t in customers:
            startTime = max(a, currTime)
            currTime = startTime + t
            totalTime += currTime - a

        return totalTime / n
