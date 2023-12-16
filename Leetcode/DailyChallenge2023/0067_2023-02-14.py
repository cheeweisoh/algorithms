class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """Add Binary

        Args:
            a (str): binary string
            b (str): binary string

        Returns:
            str: sum of a and b as a binary string
        """
        carry = 0
        ans = []
        
        if len(a) < len(b):
            a = ('0' * (len(b) - len(a))) + a
        else:
            b = ('0' * (len(a) - len(b))) + b
        
        for i in range(len(a)-1, -1, -1):
            curr_a = int(a[i])
            curr_b = int(b[i])
            
            total = curr_a + curr_b + carry
            
            ans.append(str(total % 2))
            carry = total // 2
            
        if carry:
            ans.append('1')
                    
        return ''.join(reversed(ans))