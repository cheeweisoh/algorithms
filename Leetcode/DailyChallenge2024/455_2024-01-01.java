import java.util.Arrays;

class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int gi = 0, si = 0;
        int gl = g.length, sl = s.length;
        int ans = 0;

        while (gi < gl && si < sl) {
            if (g[gi] <= s[si]) {
                ans++;
                gi++;
            }
            si++;
        }

        return ans;
    }
}
