class Solution:
    def shuffle(self, nums: list, n: int) -> list:
        """Shuffle the Array

        Args:
            nums (list): list of numbers in the form [x1,x2,...,xn,y1,y2,...,yn]
            n (int): 2n is the length of nums

        Returns:
            ans (list): returns the array in the form [x1,y1,x2,y2,...,xn,yn]
        """
        ans = []
        
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
            
        return ans