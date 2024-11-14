import math


class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        # time complexity = O(m * lg(max(quantities)))

        # if same number of stores as items, no way to further distribute
        if n == len(quantities):
            return max(quantities)

        quantities.sort(reverse=True)
        l, r = 1, quantities[0]

        while l <= r:
            # mid is the max number you want to distribute to each store
            mid = (l + r) // 2
            curr_stores = n

            # calculate the number of stores needed to get mid as answer
            for q in quantities:
                curr_stores -= math.ceil(q / mid)

            if curr_stores < 0:
                # if too many stores required, increase mid
                l = mid + 1
            else:
                # if too little stores required, decrease mid
                r = mid - 1
                res = mid

        return res
