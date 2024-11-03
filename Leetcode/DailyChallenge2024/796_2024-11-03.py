class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return s in goal + goal if len(s) == len(goal) else False
