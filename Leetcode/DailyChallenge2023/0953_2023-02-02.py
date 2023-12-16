class Solution:
    def isAlienSorted(self, words: list, order: str) -> bool:
        """Verifying an Alien Dictionary

        Args:
            words (list): sequence of strings
            order (str): lexicographical order of alien language

        Returns:
            bool: true if words are sorted lexicographically in the alien language, false otherwise
        """
        mapping = {}
        
        for i in range(len(order)):
            mapping[order[i]] = i
            
        for j in range(len(words)-1):
            word1 = words[j]
            word2 = words[j+1]
            sameword = True
            
            for k in range(min(len(word1), len(word2))):
                if word1[k] == word2[k]:
                    continue
                elif mapping[word1[k]] > mapping[word2[k]]:
                    return False
                else:
                    sameword = False
                    break
            
            if sameword and len(word1) > len(word2):
                return False
        
        return True