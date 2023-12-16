class Solution:    
    def findMinArrowShots(self, points: list) -> int:
        """Minimum Number of Arrows to Burst Balloons

        Args:
            points (list): points[i] = [x_start, x_end] denotes a balloon whose horizontal diameter stretches between x_start and x_end

        Returns:
            count (int): minimum number of arrows that must be shot to burst all balloons
        """
        points.sort(key=lambda x: x[1])
        count, arrow = 1, points[0][1]
        
        for start, end in points:
            if start > arrow:
                count += 1
                arrow = end
        
        return count