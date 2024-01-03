import collections
import math
import random
import heapq
import string


class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        ans = 0
        prev = 0
        
        for i in bank:
           curr = i.count('1')
           
           if curr == 0:
               continue
           
           ans += prev * curr
           print(curr, prev, ans)
           prev = curr
           
        return ans

def main():
    soln = Solution()
    for bank in [["011001","000000","010100","001000"], ["000","111","000"]]:
        print(soln.numberOfBeams(bank))

if __name__ == "__main__":
    main()

