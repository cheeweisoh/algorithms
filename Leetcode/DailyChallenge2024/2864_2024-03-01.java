class Solution{
    public String maximumOddBinaryNumber(String s) {
        int countZero = 0;
        int countOne = 0;

        for (char i : s.toCharArray()) {
            if (i == '0') {
                countZero++;
            }
            else {
                countOne++;
            }
        }

        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < countOne - 1; i++) {
            ans.append('1');
        }
        for (int i = 0; i < countZero; i++) {
            ans.append('0');
        }
        ans.append('1');

        return ans.toString();
    }
}