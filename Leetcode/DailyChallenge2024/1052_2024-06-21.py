class Solution:
    def maxSatisfied(
        self, customers: list[int], grumpy: list[int], minutes: int
    ) -> int:
        ans = 0
        total = sum((1 - grumpy[i]) * customers[i] for i in range(len(customers)))
        
        windowAll = 0
        windowPartial = 0

        for i in range(len(customers)):
            windowAll += customers[i]
            windowPartial += (1 - grumpy[i]) * customers[i]

            if i + 1 >= minutes:
                ans = max(ans, total - windowPartial + windowAll)
                left = i - minutes + 1
                windowAll -= customers[left]
                windowPartial -= (1 - grumpy[left]) * customers[left]

        return ans
