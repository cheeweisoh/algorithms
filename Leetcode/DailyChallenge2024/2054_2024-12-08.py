import bisect


class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        """
        time complexity: O(n log n)

        first iteration: O(n)
        second iteration: O(n)
        binary search: O(log n)
        """

        events.sort(key=lambda x: x[1])
        curr_max = []
        curr_max_val = 0
        res = 0

        # for each end time, calculate the max value up till that time
        for _, e, v in events:
            curr_max_val = max(curr_max_val, v)
            curr_max.append((e, curr_max_val))

        # for each event, check whether including that event only is a maximum
        for s, _, v in events:
            res = max(res, v)

            # do binary search to find the latest end time that doesnt overlap with the curr event start time
            idx = bisect.bisect_left(curr_max, (s, 0)) - 1
            if idx >= 0:
                # check if the combination of two events is a maximum
                res = max(res, v + curr_max[idx][1])

        return res
