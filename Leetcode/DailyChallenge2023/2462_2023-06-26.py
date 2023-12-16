import heapq

class Solution:
    def totalCost(self, costs: list, k: int, candidates: int) -> int:
        """Total Cost to Hire K Workers

        Args:
            costs (list): costs[i] is the cost of hiring the i-th worker
            k (int): number of workers to hire
            candidates (int): number of workers from left or right of costs to pick from each session

        Returns:
            total_cost (int): total cost to hire exactly k workers
        """
        total_cost = 0
        n = len(costs)
        left = candidates
        right = n - candidates
        
        left_heap = costs[:candidates]
        heapq.heapify(left_heap)
        right_heap = costs[max(candidates, n-candidates):]
        heapq.heapify(right_heap)
        
        for _ in range(k):
            if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
                cost = heapq.heappop(left_heap)
                total_cost += cost
                
                if left < right:
                    heapq.heappush(left_heap, costs[left])
                    left += 1
            else:
                cost = heapq.heappop(right_heap)
                total_cost += cost
                
                if left < right:
                    heapq.heappush(right_heap, costs[right-1])
                    right -= 1
                    
        return total_cost