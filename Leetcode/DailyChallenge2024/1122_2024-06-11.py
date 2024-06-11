class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        posDict = {}

        for pos, num in enumerate(arr2):
            posDict[num] = pos

        for num in arr1:
            if num not in posDict.keys():
                posDict[num] = 1001 + num

        ans = sorted(arr1, key=lambda x: posDict[x])
        return ans
