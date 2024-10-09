class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        moves = 0

        for i in s:
            if i == ")" and count:
                count -= 1
            elif i == ")":
                moves += 1
            else:
                count += 1

        return moves + abs(count)
