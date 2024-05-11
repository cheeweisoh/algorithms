import heapq


class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        wageQualityRatio = sorted([(w / q, q) for w, q in zip(wage, quality)])
        maxHeap = []
        maxRatio = 0.0
        qualitySum = 0

        for i in range(k):
            maxRatio = max(maxRatio, wageQualityRatio[i][0])
            qualitySum += wageQualityRatio[i][1]
            heapq.heappush(maxHeap, -wageQualityRatio[i][1])

        res = maxRatio * qualitySum

        for i in range(k, len(wageQualityRatio)):
            maxRatio = max(maxRatio, wageQualityRatio[i][0])
            qualitySum += wageQualityRatio[i][1] - (-heapq.heappop(maxHeap))
            heapq.heappush(maxHeap, -wageQualityRatio[i][1])
            res = min(res, maxRatio * qualitySum)

        return res
