class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        """
        time complexity = O(n)
        each for-loop loops through all boxes = O(n)
        """
        ls, rs = [0], [0]

        # calculate the number of operations needed to move everything to the left of the curr index to the curr index
        curr = 0
        for i in boxes[:-1]:
            if i == "1":
                curr += 1
            ls.append(ls[-1] + curr)

        # repeat the same for the right side
        curr = 0
        for i in boxes[:0:-1]:
            if i == "1":
                curr += 1
            rs.append(rs[-1] + curr)
        # need to reverse the list as we are appending left to right
        rs = rs[::-1]

        res = []

        # for each index, answer is the sum of the number of moves for the boxes to the left and right
        for i in range(len(boxes)):
            res.append(ls[i] + rs[i])

        return res
