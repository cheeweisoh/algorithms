class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        completeCycle = n * 2 - 2
        remainTime = time % completeCycle
        noDiff = abs(n - 1 - remainTime)
        noFromStart = n - noDiff

        return noFromStart
