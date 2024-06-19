class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        l, r = 1, 1000000000
        ans = -1

        while l <= r:
            mid = l + (r - l) // 2
            consecLength, bouquets = 0, 0
            for bloom in bloomDay:
                if bloom <= mid:
                    consecLength += 1
                    if consecLength >= k:
                        consecLength = 0
                        bouquets += 1
                else:
                    consecLength = 0

            if bouquets >= m:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans
