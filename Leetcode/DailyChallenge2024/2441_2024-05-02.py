class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        map = {}
        ans = -1
        
        for i in nums:
            if abs(i) in map and i != map[abs(i)]:
                ans = max(abs(i), ans)
            else:
                map[abs(i)] = i
        
        return ans