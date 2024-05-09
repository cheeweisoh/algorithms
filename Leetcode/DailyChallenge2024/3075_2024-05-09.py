class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse=True)
        totalSum = 0
        turns = 0

        for i in range(k):
            totalSum += max(happiness[turns] - turns, 0)
            turns += 1

        return totalSum
