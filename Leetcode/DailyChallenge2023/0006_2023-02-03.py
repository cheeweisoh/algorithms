class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """Zigzag Conversion

        Args:
            s (str): input string
            numRows (int): number of rows in zigzag pattern

        Returns:
            ans (str): makes conversion to zigzag pattern and return flattened output
        """
        if len(s) == 1 or numRows == 1:
            return s
        
        zigzag = [''] * numRows
        curr = 0
        dir = 1
        
        for i in range(len(s)):
            zigzag[curr] += s[i]
            curr += dir
            
            if curr == 0 or curr == numRows-1:
                dir *= -1
                
        ans = ''.join(zigzag)
        
        return ans