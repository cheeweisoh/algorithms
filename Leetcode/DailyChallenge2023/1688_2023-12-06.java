class Solution {
    public int numberOfMatches(int n) {
        int ans = 0;
        int remain = n;

        while(remain > 1){
          ans += remain / 2;

          if(remain%2 == 1){
            remain = remain / 2 + 1;
          }
          else {
            remain = remain / 2;
          }
        }
        return ans;
    }
}