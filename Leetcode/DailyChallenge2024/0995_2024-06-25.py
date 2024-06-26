class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # flipped is the reference to be checked against to determine if number has to be flipped
        # if nums[i] is the same as flipped then it has to be flipped
        flipped = 0
        ans = 0
        # fp stores whether there has been a flip at index i
        fp = [0] * n

        for i in range(n):
            if i >= k:
                # if curr index is more than k, we might have to flip the reference
                # depending on whether there was a flip at [i-k]
                # since the [i-k] flip does not affect nums[i]
                flipped ^= fp[i - k]
            if flipped == nums[i]:
                # if i + k > n, there is not enough room for a k flip at index i
                if i + k > n:
                    return -1
                fp[i] = 1
                flipped ^= 1
                ans += 1

        return ans
