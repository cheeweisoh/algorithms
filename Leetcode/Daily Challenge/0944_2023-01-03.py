class Solution:
    def minDeletionSize(self, strs: list) -> int:
        """Delete Columns to Make Sorted

        Args:
            strs (list): list of strings, all of same length

        Returns:
            count (int): number of columns that are not in lexicographic order
        """
        count = 0
        
        for j in range(len(strs[0])):
            for i in range(1,len(strs)):
                if strs[i][j] < strs[i-1][j]:
                    count += 1
                    break
        
        return count