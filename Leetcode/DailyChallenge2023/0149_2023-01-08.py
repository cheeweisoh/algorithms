import collections
import math

class Solution:
    def maxPoints(self, points: list) -> int:
        """Max Points on a Line

        Args:
            points (list): [x_i, y_i] represents a point on the X-Y plane

        Returns:
            count (int): maximum number of points that lie on the same straight line
        """
        if len(points) <= 2:
            return len(points)
        
        points.sort(key=lambda x: x[0])
        count = 0
        
        for i in range(len(points)-1):
            gradient = collections.defaultdict(int)
            
            for j in range(i+1, len(points)):
                x_i, y_i = points[i][0], points[i][1]
                x_j, y_j = points[j][0], points[j][1]
                
                if x_i == x_j:
                    grad = math.inf
                else:
                    grad = (y_j - y_i)/(x_j - x_i)
                gradient[grad] += 1
            
            count = max(count, max(gradient.values())+1)
        return count