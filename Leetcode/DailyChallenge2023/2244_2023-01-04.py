import collections

class Solution:    
    def minimumRounds(self, tasks: list) -> int:
        """Minimum Rounds to Complete All Tasks

        Args:
            tasks (list):  0-indexed integer array, where tasks[i] represents the difficulty level of a task

        Returns:
            rounds (int): minimum rounds required to complete all the tasks, or -1 if it is not possible
        """
        store = collections.defaultdict(int)
        rounds = 0
        
        for i in range(len(tasks)):
            store[tasks[i]] += 1
            
        for j in store.values():
            if j == 1:
                return -1
            elif j % 3 == 0:
                rounds += j // 3
            else:
                rounds += 1 + (j // 3)
            
        return rounds