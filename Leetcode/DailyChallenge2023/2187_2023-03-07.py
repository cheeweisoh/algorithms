class Solution:
    def minimumTime(self, time: list, totalTrips: int) -> int:
        """Minimum Time to Complete Trips

        Args:
            time (list): time[i] denotes time taken by i-th bus to complete one trip
            totalTrips (int): number of trips all buses should make in total

        Returns:
            int: minimum time required for all buses to complete at least totalTrips trips
        """
        l = 1
        r = min(time) * totalTrips
        
        while l < r:
            mid = (l + r) // 2
            
        if sum(mid//t for t in time) >= totalTrips:
            r = mid
        else:
            l = mid + 1
            
        return l