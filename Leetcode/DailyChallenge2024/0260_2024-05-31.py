class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xorSum = 0
        for n in nums:
            xorSum ^= n

        setBit = xorSum & -xorSum

        a, b = 0, 0
        for n in nums:
            if n & setBit:
                a ^= n
            else:
                b ^= n

        return [a, b]
