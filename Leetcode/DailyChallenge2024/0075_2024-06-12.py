class Solution:
    def sortColors(self, nums: list[int]) -> None:
        count, idx = 0, 0

        while count < len(nums):
            if nums[idx] == 0:
                nums.pop(idx)
                nums.insert(0, 0)
                idx += 1
            elif nums[idx] == 2:
                nums.pop(idx)
                nums.insert(len(nums), 2)
            else:
                idx += 1
            count += 1
