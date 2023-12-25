import collections
import math
import random
import heapq
import string

class Solution:
    def numDecodings(self, s: str) -> int:
        
        def dfs(s):
            if s == '':
                return 1
            
            ways = 0
            
            for i in range(len(s)):
                cs = s[:i+1]
                
                if cs[0] == '0' or int(cs) > 26:
                   break
                
                ways += dfs(s[i+1:])
            
            return ways
        
        return dfs(s) 

def main():
    soln = Solution()
    
    for i in ["12", "226", "06"]:
        print(soln.numDecodings(i))

if __name__ == "__main__":
    main()