class Solution:
    def __init__(self):
        self.mapping = {}
        
    def find(self, s: str) -> str:
        self.mapping.setdefault(s, s)
        
        if s != self.mapping[s]:
            self.mapping[s] = self.find(self.mapping[s])
        return self.mapping[s]
        
    def union(self, s1: str, s2: str) -> None:
        root_s1 = self.find(s1)
        root_s2 = self.find(s2)
        
        if root_s1 > root_s2:
            self.mapping[root_s1] = root_s2
        else:
            self.mapping[root_s2] = root_s1
    
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """Lexicographically Smallest Equivalent String

        Args:
            s1 (str): string 1
            s2 (str): string 2
            baseStr (str): base string

        Returns:
            ans (str): lexicographically smallest equivalent string of baseStr by using equivalency information from s1 and s2
        """
        for i in range(len(s1)):
            self.union(s1[i], s2[i])
            print(self.mapping)
        
        ans = ''
        
        for j in baseStr:
            ans += self.find(j)
            
        return ans