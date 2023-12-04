import collections

class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        mapping = collections.Counter(p)
        w = len(p)
        check = 0
        ans = []
        
        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] == 0:
                    check -= 1
                mapping[s[i]] -= 1
                if mapping[s[i]] == 0:
                    check += 1
                    
            if i >= w and s[i-w] in mapping:
                if mapping[s[i-w]] == 0:
                    check -= 1
                mapping[s[i-w]] += 1
                if mapping[s[i-w]] == 0:
                    check += 1
            
            if check == len(mapping):
                ans.append(i-w+1)
                
        return ans