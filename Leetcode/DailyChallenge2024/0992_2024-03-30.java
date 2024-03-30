import java.util.HashMap;

class Solution {
    public int subarraysWithKDistinct(int[] nums, int k) {
        int subarrayWithAtMostK = subarraysWithAtMostN(nums, k);
        int subarrayWithAtMostKMinusOne = subarraysWithAtMostN(nums, k - 1);
        return (subarrayWithAtMostK - subarrayWithAtMostKMinusOne);
    }

    public int subarraysWithAtMostN(int[] nums, int n){
       HashMap<Integer, Integer> map = new HashMap<>();
       int left = 0, right = 0, ans = 0;

       while (right < nums.length) {
           map.put(nums[right], map.getOrDefault(nums[right], 0) + 1);

           while (map.size() > k) {
               map.put(nums[left], map.get(nums[left]) - 1);
               if (map.get(nums[left]) == 0) {
                   map.remove(nums[left]);
               }
               left++;
           }

           ans += right - left + 1;
           right++;
       }

       return ans;
    }
}
