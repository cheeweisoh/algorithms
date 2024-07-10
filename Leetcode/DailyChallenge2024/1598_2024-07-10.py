class Solution:
    def minOperations(self, logs: list[str]) -> int:
        count = 0

        for i in logs:
            if i == "./":
                print(count)
                continue
            elif i == "../":
                count = max(count - 1, 0)
            else:
                count += 1

        return max(count, 0)
