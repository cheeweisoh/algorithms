class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        items.sort(key=lambda x: x[0])
        queries_sort = [[i, q] for i, q in enumerate(queries)]
        queries_sort.sort(key=lambda x: x[1])

        res = [0] * len(queries)
        c = 0
        curr_max = 0

        for pos, q in queries_sort:
            while c < len(items) and q >= items[c][0]:
                curr_max = max(curr_max, items[c][1])
                c += 1
            res[pos] = curr_max

        return res
