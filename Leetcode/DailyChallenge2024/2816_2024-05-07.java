class Solution {
    public ListNode doubleIt(ListNode head) {
        ListNode prev = null, curr = head;

        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        
        int carry = Math.floorDiv(prev.val * 2, 10);
        prev.val = (prev.val * 2) % 10;
        curr = prev.next;
        prev.next = null;

        while (curr != null) {
            ListNode next = curr.next;

            int doubledVal = curr.val * 2 + carry;
            int base = doubledVal % 10;
            carry = Math.floorDiv(doubledVal, 10);
            curr.val = base;

            System.out.println(doubledVal);
            System.out.println(base);
            System.out.println(carry);

            curr.next = prev;
            prev = curr;
            curr = next;
        }

        if (carry != 0) {
            ListNode extraNode = new ListNode(carry);
            extraNode.next = prev;
            prev = extraNode;
        }

        return prev;
    }
}
