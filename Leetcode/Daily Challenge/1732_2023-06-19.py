class Solution:
    def largestAltitude(self, gain: list) -> int:
        """Find the Highest Altitude

        Args:
            gain (list): gain[i] is the net gain in altitude between points i and i+1

        Returns:
            max_alt (int): highest altitude of a point
        """
        curr_alt = 0
        max_alt = 0
        
        for i in gain:
            curr_alt = curr_alt + i
            max_alt = max(max_alt, curr_alt)
            
        return max_alt