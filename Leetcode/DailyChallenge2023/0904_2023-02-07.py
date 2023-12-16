import collections

class Solution:
    def totalFruit(self, fruits: list) -> int:
        """Fruit Into Baskets

        Args:
            fruits (list): integer array where fruits[i] is the type of fruit the i-th tree produces

        Returns:
            ans (int): maximum number of fruits you can pick 
        """
        curr_fruits = collections.defaultdict(int)
        s = 0
        
        for e in range(len(fruits)):
            curr_fruits[fruits[e]] += 1
            
            if len(curr_fruits) > 2:
                curr_fruits[fruits[s]] -= 1
                
                if curr_fruits[fruits[s]] == 0:
                    del curr_fruits[fruits[s]]
                
                s += 1
        
        ans = e - s + 1
        return ans