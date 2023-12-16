class Solution:
    def getAverages(self, nums: list, k: int) -> list:
        """K Radius Subarray Averages

        Args:
            nums (list): 0-indexed array of n integers
            k (int): integer

        Returns:
            avgs (list): avgs[i] is the k-radius average for the subarray centered at index i
        """
        n = len(nums)
        r = 2*k+1
        
        if n < r:
            return [-1]*n
        
        temp = sum(nums[:r])
        avgs = [temp//r]
        
        for i in range(k+1, n-k):
            temp -= nums[i-k-1]
            temp += nums[i+k]
            avgs.append(temp // r)
        
        avgs = [-1]*k + avgs + [-1]*k
        return avgs