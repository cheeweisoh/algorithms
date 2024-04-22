import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;
import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int openLock(String[] deadends, String target) {
        Set<String> deadendSet = new HashSet<>(Arrays.asList(deadends));
        if (deadendSet.contains("0000")) {
            return -1;
        }

        Queue<Pair<String, Integer>> queue = new LinkedList<>();
        queue.offer(new Pair<>("0000", 0));
        Set<String> visited = new HashSet<>();
        visited.add("0000");

        while (!queue.isEmpty()) {
            Pair<String, Integer> curr = queue.poll();
            String currCombi = curr.getKey();
            int currMoves = curr.getValue();

            if (currCombi.equals(target)) {
                return currMoves;
            }

            for (int i = 0; i < 4; i++) {
                for (int delta : new int[]{-1, 1}) {
                    int newDigit = (currCombi.charAt(i) - '0' + delta + 10) % 10;
                    String newCombi = currCombi.substring(0, i) + newDigit + currCombi.substring(i + 1);

                    if (!visited.contains(newCombi) && !deadendSet.contains(newCombi)) {
                        queue.offer(new Pair<>(newCombi, currMoves + 1));
                        visited.add(newCombi);
                    }
                }
            }
        }

        return -1;
    }
}
