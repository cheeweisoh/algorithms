import heapq

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        heap = []

        for i, s in enumerate(score):
            heapq.heappush(heap, (-s, i))

        place = 1
        topThree = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        while heap:
            s, i = heapq.heappop(heap)
            if place <= 3:
                score[i] = topThree[place - 1]
            else:
                score[i] = str(place)

            place += 1

        return score
