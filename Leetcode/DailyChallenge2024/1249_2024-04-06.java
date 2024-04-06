class Solution {
    public String minRemoveToMakeValid(String s) {
        char [] strArr = s.toCharArray();
        int count = 0;

        for (int i = 0; i < strArr.length; i++) {
            if (strArr[i] == '(') {
                count++;
            } else if (strArr[i] == ')' && count == 0) {
                strArr[i] = '*';
            } else if (strArr[i] == ')') {
                count--;
            }
        }

        for (int i = strArr.length - 1; i >= 0; i--) {
            if (strArr[i] == '(' && count > 0) {
                strArr[i] = '*';
                count--;
            }
        }

        int p = 0;
        for (int i = 0; i < strArr.length; i++) {
            if (strArr[i] != '*') {
                strArr[p++] = strArr[i];
            }
        }

        String ans = new String(strArr).substring(0, p);

        return ans;
    }
}
