import java.util.Arrays;

class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] taskFreq = new int[26];
        for (char task : tasks) {
            taskFreq[task - 'A']++;
        }

        Arrays.sort(taskFreq);
        int lastFreq = 0;
        int maxFreq = taskFreq[25];

        for (int i : taskFreq) {
            if (i == maxFreq) {
                lastFreq++;
            }
        }

        int count = ((maxFreq - 1) * (n + 1)) + lastFreq;
        
        return Math.max(count, tasks.length);
    }
}