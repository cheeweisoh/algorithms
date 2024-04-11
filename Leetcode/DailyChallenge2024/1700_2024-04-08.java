class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        int[] studentCounts = new int[2];
        for (int st : students) {
            studentCounts[st]++;
        }
        
        int remain = sandwiches.length;
        for (int sw : sandwiches) {
            if (studentCounts[sw] > 0) {
                studentCounts[sw]--;
                remain--;
            } else {
                break;
            }
        }

        return remain;
    }
}
