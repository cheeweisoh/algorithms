class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        n = len(arr)
        pref, suff = 0, 0

        for i in range(0, n - 1):
            if arr[i] > arr[i + 1]:
                pref = i
                break
        for j in range(n - 1, 0, -1):
            if arr[j] < arr[j - 1]:
                suff = j
                break

        if pref == 0 and suff == 0:
            return 0

        res = min(n - pref - 1, suff)

        i, j = 0, suff
        while i <= pref and j < n:
            if arr[i] <= arr[j]:
                res = min(res, j - i - 1)
                i += 1
            else:
                j += 1

        return res
