import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean halvesAreAlike(String s) {
        String leftString = s.substring(0, s.length()/2).toLowerCase();
        String righString = s.substring(s.length()/2).toLowerCase();
        Set<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');

        int leftVowel = 0;
        int rightVowel = 0;

        for (char i : leftString.toCharArray()) {
            if (vowels.contains(i)) {
                leftVowel ++;
            }
        }

        for (char j : righString.toCharArray()) {
            if (vowels.contains(j)) {
                rightVowel ++;
            }
        }

        return leftVowel == rightVowel;
    }
}