class Solution:
    def sortVowels(self, s: str) -> str:
        """Sort Vowels in a String

        Args:
            s (str): string

        Returns:
            str: new string such that all consonants must remain in their current position and vowels must be sorted in nondecreasing ASCII order
        """
        all_vowels = set('AEIOUaeiou')
        vowels = [i for i in s if i in all_vowels]
        vowels.sort()
        idx = 0
        ans = ''
        
        for i in s:
            if i in all_vowels:
                ans += vowels[idx]
                idx += 1
            else:
                ans += i
                    
        return ans