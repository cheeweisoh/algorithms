import collections
import math
import random
import heapq
import string

class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        total_time = 0
        curr_time = [neededTime[0],]
        
        for i in range(len(colors)-1):
            if colors[i] == colors[i+1]:
                curr_time.append(neededTime[i+1])
            else:
                total_time += sum(curr_time) - max(curr_time)
                curr_time = [neededTime[i+1],]
        
        total_time += sum(curr_time) - max(curr_time) if len(curr_time) > 1 else 0
        
        return total_time

def main():
    soln = Solution()
    
    for c, t in [["abaac", [1,2,3,4,5]], ["abc", [1,2,3]], ["aabaa", [1,2,3,4,1]], ["aaaba", [1,2,3,4,5]]]:
        print(soln.minCost(c, t))

if __name__ == "__main__":
    main()