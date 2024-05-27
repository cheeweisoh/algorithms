class Solution:
    def specialArray(self, nums: list[int]) -> int:
        counts = [0] * (len(nums) + 1)

        for i in nums:
            if i >= len(counts):
                counts = [x + 1 for x in counts]
            else:
                counts[: i + 1] = [x + 1 for x in counts[: i + 1]]
        print(counts)

        for j in range(len(counts)):
            if j == counts[j]:
                return j

        return -1
