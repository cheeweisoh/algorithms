class Solution:
    def __init__(self):
        self.mem = [0] * 38
        self.mem[1] = 1
        self.mem[2] = 1
    
    def tribonacci(self, n: int) -> int:
        """N-th Tribonacci Number

        Args:
            n (int): interger (from 0 to 37)

        Returns:
            ans (int): n-th tribonacci number given by T_(n+3) = T_(n) + T_(n+1) + T_(n+2) for n >= 0
        """
        if self.mem[n] or n == 0:
            return self.mem[n]
        
        ans = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        self.mem[n] = ans
        return ans