class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        """
        time complexity = O(m+n)
        first for-loop = O(m), m = len(shifts)
        second for-loop = O(n), n = len(s)
        """

        prefix_sum = [0] * (len(s) + 1)

        # construct prefix sum, only accounting for the change at the start and end pos
        # to avoid an inner for-loop
        for start, end, dir in shifts:
            change = 1 if dir else -1
            prefix_sum[start] += change
            prefix_sum[end + 1] -= change

        # keep track of current change
        res = list(s)
        curr = 0
        for i in range(len(s)):
            curr += prefix_sum[i]
            # loop back to start of alphabet if change exceeds
            res[i] = chr(ord("a") + (ord(res[i]) - ord("a") + curr) % 26)

        return "".join(res)
