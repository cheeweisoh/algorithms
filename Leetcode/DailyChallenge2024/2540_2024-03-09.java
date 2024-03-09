class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        int pOne = 0;
        int pTwo = 0;

        while (pOne < nums1.length && pTwo < nums2.length) {
            if (nums1[pOne] == nums2[pTwo]) {
                return nums1[pOne];
            } else if (nums1[pOne] > nums2[pTwo]) {
                pTwo++;
            } else {
                pOne++;
            }
        }
        return -1;
    }
}