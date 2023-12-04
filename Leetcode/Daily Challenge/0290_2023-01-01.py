class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """Word Pattern

        Args:
            pattern (str): pattern
            s (str): string

        Returns:
            bool: returns True if s follows the same pattern, False otherwise
        """
        mapping = {}
        words = s.split(sep = ' ')
        
        if len(words) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]
            
            if p in mapping:
                if mapping[p] != w:
                    return False
            elif w in mapping.values():
                return False
            else:
                mapping[p] = w
                
        return True