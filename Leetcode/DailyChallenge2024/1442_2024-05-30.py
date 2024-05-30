class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        n = len(arr)
        ans = 0
        xorArray = [0, arr[0]]
        for i in range(1, n):
           xorArray.append(xorArray[-1] ^ arr[i]) 

        for i in range(n):
            for k in range(i+1, n):
                if xorArray[i] == xorArray[k+1]:
                    ans += (k - i)
        
        return ans