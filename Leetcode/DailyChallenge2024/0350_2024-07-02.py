import collections


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        counts = collections.defaultdict(int)
        for i in nums1:
            counts[i] += 1

        for j in nums2:
            if j in counts and counts[j] > 0:
                ans.append(j)
                counts[j] -= 1

        return ans
