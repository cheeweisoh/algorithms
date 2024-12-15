import heapq


class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        """
        time complexity: O((n+k) log n)
        n = no of classes
        k = no of extra students

        first for loop: O(n)
        second for loop: O(k)
        heap push and pull: O(log n)
        """
        h = []

        # push to a heap the change in ratio when adding a new student
        for p, t in classes:
            heapq.heappush(h, (p / t - ((p + 1) / (t + 1)), p, t))

        # pop the class with the largest change and add one student
        for _ in range(extraStudents):
            _, cp, ct = heapq.heappop(h)
            heapq.heappush(
                h, ((cp + 1) / (ct + 1) - (cp + 2) / (ct + 2), cp + 1, ct + 1)
            )

        # calculate average ratio
        res = 0
        for _, cp, ct in h:
            res += cp / ct

        return res / len(classes)
