class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character, Integer> l = new HashMap<>();

        for (char a : s.toCharArray()) {
            l.put(a, l.getOrDefault(a, 0) + 1);
        }

        for (int i = 0; i < s.length(); i++) {
            if (l.get(s.charAt(i)) == 1) {
                return i;
            }
        }

        return -1;
    }
}
