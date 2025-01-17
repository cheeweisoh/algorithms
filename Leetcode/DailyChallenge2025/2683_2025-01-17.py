class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        """
        time complexity: O(n)
        """
        res = 0

        # take the XOR of each element in the array
        for i in derived:
            res ^= i

        # since each element in the original array is used twice
        # the XOR of all elements in the derived array should be 0
        return res == 0
