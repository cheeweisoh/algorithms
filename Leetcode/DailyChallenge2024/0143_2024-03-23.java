class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) {
            return;
        }

        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode prev = null, next = null;
        while (slow != null) {
            next = slow.next;
            slow.next = prev;
            prev = slow;
            slow = next;
        }

        ListNode firstHalf = head, secondHalf = prev;
        while (secondHalf.next != null) {
            next = firstHalf.next;
            prev = secondHalf.next;

            firstHalf.next = secondHalf;
            secondHalf.next = next;

            firstHalf = next;
            secondHalf = prev;
        }
    }
}
