class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        """Minimum Time Visiting All Points

        Args:
            points (list[list[int]]): list of points in integer coordinates

        Returns:
            int: time taken to pass through all points in order
        """
        time = 0
        [curr_x, curr_y] = points[0]
        
        for new_x, new_y in points[1:]:
            time += max(abs(new_x - curr_x), abs(new_y - curr_y))
            curr_x, curr_y = new_x, new_y
            
        return time