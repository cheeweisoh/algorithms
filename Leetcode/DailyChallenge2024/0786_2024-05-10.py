class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        stack = []
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                frac = arr[i]/ arr[j]
                heapq.heappush(stack, [frac, arr[i], arr[j]])
                
        for l in range(k):
            frac, i, j = heapq.heappop(stack)
            print(frac, i, j)
            
        return [i, j]