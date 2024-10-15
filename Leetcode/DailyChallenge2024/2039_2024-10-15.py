class Solution:
    def minimumSteps(self, s: str) -> int:
        steps, blacks = 0, 0
        for i in s:
            if i == "0":
                steps += blacks
            else:
                blacks += 1

        return steps
