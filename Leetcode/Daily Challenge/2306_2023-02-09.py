class Solution:
    def distinctNames(self, ideas: list) -> int:
        """Naming a company

        Args:
            ideas (list): list of names

        Returns:
            ans (int): number of distinct valid names
        """
        ans = 0
        suffixes = [set() for _ in range(26)]
        
        for i in range(25):
            for j in range(i+1, 26):
                count = len(suffixes[i] & suffixes[j])
                ans += 2 * (len(suffixes[i]) - count) * (len(suffixes[j]) - count)
                
        return ans