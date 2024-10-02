class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {i: x for x, i in enumerate(sorted(set(arr)))}
        res = [ranks[j] + 1 for j in arr]

        return res
