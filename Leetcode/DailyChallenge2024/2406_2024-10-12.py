class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)
        curr_end = 0
        res = 0

        for s in start_times:
            if s > end_times[curr_end]:
                curr_end += 1
            else:
                res += 1

        return res
