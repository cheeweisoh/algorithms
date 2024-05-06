// Remove Nodes from Linked List

class Solution {
    public ListNode removeNodes(ListNode head) {
        ListNode prev = null, curr = head;

        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        
        curr = prev.next;
        prev.next = null;

        while (curr != null) {
            ListNode next = curr.next;
            
        if (curr.val >= prev.val) {
                curr.next = prev;
                prev = curr;
            }
            curr = next;
        }

        return prev;
    }
}
