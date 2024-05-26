class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        dpLast = [[0 for _ in range(3)] for _ in range(2)]
        dpCurr = [[0 for _ in range(3)] for _ in range(2)]
        dpLast[0][0] = 1

        for _ in range(n):
            for a in range(2):
                for l in range(3):
                    # choose P
                    dpCurr[a][0] = (dpCurr[a][0] + dpLast[a][l]) % MOD
                    # choose A
                    if a == 0:
                        dpCurr[a + 1][0] = (dpCurr[a + 1][0] + dpLast[a][l]) % MOD
                    # choose L
                    if l < 2:
                        dpCurr[a][l + 1] = (dpCurr[a][l + 1] + dpLast[a][l]) % MOD
            dpLast = dpCurr
            dpCurr = [[0 for _ in range(3)] for _ in range(2)]

        ans = sum(dpLast[a][l] for a in range(2) for l in range(3)) % MOD
        return ans
