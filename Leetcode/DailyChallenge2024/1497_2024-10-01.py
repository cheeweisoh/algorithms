import collections


class Solution:
    def canArrange(self, arr: list, k: int) -> bool:
        a = collections.Counter(x % k for x in arr)

        if 0 in a:
            if a[0] % 2 != 0:
                return False

        for i in a.keys():
            if i > 0:
                if a[i] != a[k - i]:
                    return False

        return True
