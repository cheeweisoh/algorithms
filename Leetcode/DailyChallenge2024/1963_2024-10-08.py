class Solution:
    def minSwaps(self, s: str) -> int:
        imbal, swap = 0, 0

        for i in s:
            if i == "[":
                imbal += 1
            elif i == "]" and imbal:
                imbal -= 1
            else:
                imbal += 1
                swap += 1

        return swap
