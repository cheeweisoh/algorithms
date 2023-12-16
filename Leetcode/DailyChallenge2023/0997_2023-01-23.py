import collections

class Solution:
    def findJudge(self, n: int, trust: list) -> int:
        """Find the Town Judge

        Args:
            n (int): number of people
            trust (list): trust[i] = [a_i, b_i] represents that person a_i trusts person b_i

        Returns:
            person (int): label of the town judge if it exists and can be identified, -1 otherwise
        """
        if n == 1:
            return n
        
        graph = collections.defaultdict(list)
        
        for person, target in trust:
            graph.setdefault(person, [0, 0])
            graph.setdefault(target, [0, 0])
            
            graph[person][0] += 1
            graph[target][1] += 1
            
        for person in graph.keys():
            if graph[person] == [0, n-1]:
                return person
        return -1