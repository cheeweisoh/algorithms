class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        l, r = 1, position[-1] - position[0]
        ans = -1

        while l < r:
            # mid is the current min distance that we are testing
            mid = l + (r - l) // 2
            lastPos, balls = position[0], 1

            for i in range(1, len(position)):
                # if the position difference between curr pos and last pos is more than the min dist, we are able to place a ball
                if position[i] - lastPos >= mid:
                    lastPos = position[i]
                    balls += 1

            # if we are able to place all m balls, the answer mid is a possible solution
            # if we are able to place more than m balls, removing (balls-m) balls would also lead to a solution
            if balls >= m:
                ans = mid
                # if it is a solution, there is possibly a solution w greater min distance than mid
                l = mid + 1
            else:
                # if there is no solution, the largest solution has to be smaller than mid
                r = mid - 1

        return ans
