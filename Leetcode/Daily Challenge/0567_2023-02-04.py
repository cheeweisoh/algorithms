import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Permutation in String

        Args:
            s1 (str): string to check
            s2 (str): string to be checked

        Returns:
            bool: returns true if one of s1's permutations is the substring of s2, false otherwise
        """
        
        mapping = collections.Counter(s1)
        w = len(s1)
        counter = 0
        
        for i in range(len(s2)):
            if s2[i] in mapping:
                if mapping[s2[i]] == 0:
                    counter -= 1
                mapping[s2[i]] -= 1
                if mapping[s2[i]] == 0:
                    counter += 1
                
            if i >= w and s2[i-w] in mapping:
                if mapping[s2[i-w]] == 0:
                    counter -= 1
                mapping[s2[i-w]] += 1
                if mapping[s2[i-w]] == 0:
                    counter += 1
                    
            if counter == len(mapping):
                return True
            
        return False