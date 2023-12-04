class SummaryRanges:
    def __init__(self):
        """Data Stream as Disjoint Intervals
        """
        self.intervals = []
    
    def addNum(self, value: int) -> None:
        """Adds interger value to the stream

        Args:
            value (int): interger to be added into the stream
        """
        if not self.intervals:
            self.intervals = [[value, value]]
        
        start = 0
        end = len(self.intervals)
        curr = 0
        
        while start < end:
            mid = (start+end) // 2
            s, e = self.intervals[mid]
            
            if s <= value and value <= e:
                return
            elif value < s:
                curr = mid
                end = mid
            elif value > e:
                curr = mid + 1
                start = mid + 1
        
        if curr == 0:
            if value < self.intervals[0][0] - 1:
                self.intervals = [[value, value]] + self.intervals
            else:
                self.intervals[0][0] = value
        elif curr == len(self.intervals):
            if value > self.intervals[-1][1] + 1:
                self.intervals = self.intervals + [[value, value]]
            else:
                self.intervals[-1][1] = value
        else:
            if self.intervals[curr-1][1] + 1 == value and self.intervals[curr][0] - 1 == value:
                self.intervals = self.intervals[:curr-1] + [[self.intervals[curr-1][0], self.intervals[curr][1]]] + self.intervals[curr+1:]
            elif self.intervals[curr-1][1] + 1 == value:
                self.intervals[curr-1][1] = value
            elif self.intervals[curr][0] - 1 == value:
                self.intervals[curr][0] = value
            else:
                self.intervals = self.intervals[:curr] + [[value, value]] + self.intervals[curr:]
        
    def getIntervals(self) -> list:
        """Returns summary of intergers in the stream currently as a list of disjoint intervals

        Returns:
            intervals (list): summary of intergers in the stream
        """
        return self.intervals