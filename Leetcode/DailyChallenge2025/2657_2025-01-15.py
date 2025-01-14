class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        """
        time complexity = O(n)
        """
        n = len(A)
        # keep a seen table for all values in the array, index corresponds to the value
        seen = [0] * (n + 1)
        res = []
        curr = 0

        for i in range(n):
            # add the current number to the seen list
            seen[A[i]] += 1
            # if the current number has already been seen once (current count = 2), add 1 to the common count
            if seen[A[i]] == 2:
                curr += 1
            seen[B[i]] += 1
            if seen[B[i]] == 2:
                curr += 1

            res.append(curr)

        return res
