class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        # time complexity = O(n)

        # if window is 1, return orig list
        if k == 1:
            return nums

        win_size = 1
        res = [-1] * (len(nums) - k + 1)
        for i in range(1, len(nums)):
            # if curr number is consecutive with prev number, increment window
            if nums[i] - nums[i - 1] == 1:
                win_size += 1
                # append last element, guranteed to be largest since window should be consecutive
                if win_size == k:
                    res[i - k + 1] = nums[i]
                    win_size -= 1
            # reset window if not consecutive, curr number is start of new window
            else:
                win_size = 1

        return res
