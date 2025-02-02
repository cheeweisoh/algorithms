class Solution:
    def check(self, nums: list[int]) -> bool:
        numss = nums + nums
        n = len(nums)

        # iterate through all possible rotated indices
        for i in range(n):
            curr = 1
            # check if the array of length n starting from i is sorted
            for j in range(1, n):
                if numss[i + j] < numss[i + j - 1]:
                    break
                else:
                    curr += 1

            # if its possible to get a sorted array, i is the index where the array was rotated
            if curr == n:
                return True

        return False
