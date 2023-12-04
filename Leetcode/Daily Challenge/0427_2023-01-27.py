class Solution:    
    def findAllConcatenatedWordsInADict(self, words: list) -> list:
        """Concatenated Words

        Args:
            words (list): list of strings without duplicates

        Returns:
            ans (list): all concatenated words in given list of words
        """
        mem = {}
        ans = []
        
        def check(word):
            if word in mem:
                return mem[word]
            
            
            for i in range(len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if not (prefix in words and (suffix in words or check(suffix))):
                    mem[word] = False
                else:
                    mem[word] = True
                    break
            
            return mem[word]
        
        for word in words:
            if check(word):
                ans.append(word)
        
        return ans