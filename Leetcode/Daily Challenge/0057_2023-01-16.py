class Solution:
    def insert(self, intervals: list, newInterval: list) -> list:
        """Insert Interval

        Args:
            intervals (list): array of non-overlapping intervals
            newInterval (list): new interval

        Returns:
            intervals (list): new invertals after inserting newInterval and merging overlapping intervals
        """
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])        
        i = 0
        
        while i < len(intervals)-1:
            x, y = intervals[i]
            if y >= intervals[i+1][0]:
                start = x
                end = max(y, intervals[i+1][1])
                intervals[i:i+2] = [[start, end]]
            else:
                i += 1
        
        return intervals