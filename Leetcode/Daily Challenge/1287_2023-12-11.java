class Solution {
    public int findSpecialInteger(int[] arr) {
        int count = 0;
        int prev_int = 0;
        int size = arr.length;

        for (int i=0; i<size; i++){
            if (arr[i] == prev_int){
                count++;
                if (count > (size / 4)) {
                    return arr[i];
                }
            }
            else {
                count = 1;
            }
            prev_int = arr[i];
        }

        return prev_int;
    }
}