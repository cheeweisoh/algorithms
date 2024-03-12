import java.util.HashMap;
import java.util.Map;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}


class Solution {
    public ListNode removeZeroSumSublists(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        int prefixSum = 0;
        Map<Integer, ListNode> prefixSums = new HashMap<>();

        for (ListNode curr = dummy; curr != null; curr = curr.next) {
            prefixSum += curr.val;

            if (prefixSums.containsKey(prefixSum)) {
                ListNode prev = prefixSums.get(prefixSum);
                ListNode remv = prev.next;
                int p = prefixSum + (remv != null ? remv.val : 0);

                while (p != prefixSum) {
                    prefixSums.remove(p);
                    remv = remv.next;
                    p += (remv != null ? remv.val : 0);
                }

                prev.next = curr.next;
            } else{
                prefixSums.put(prefixSum, curr);
            }
        }

        return dummy.next;
    }
}