import heapq

class Solution:
    def kSmallestPairs(self, nums1: list, nums2: list, k: int) -> list:
        """Find k Pairs With Smallest Sums

        Args:
            nums1 (list): integer array in ascending order
            nums2 (list): integer array in ascending order
            k (int): number of pairs

        Returns:
            ans (list): k pairs of integers (with one from each array) with the smallest sums
        """
        heap = []
        heapq.heappush(heap, (nums1[0]+nums2[0], 0, 0))
        ans = []
        
        while heap and len(ans) < k:
            _, l, r = heapq.heappop(heap)
            ans.append([nums1[l], nums2[r]])
            
            if l+1 < len(nums1):
                heapq.heappush(heap, (nums1[l+1] + nums2[r], l+1, r))
            if l == 0 and r+1 < len(nums2):
                heapq.heappush(heap, (nums1[l] + nums2[r+1], l, r+1))
        
        return ans