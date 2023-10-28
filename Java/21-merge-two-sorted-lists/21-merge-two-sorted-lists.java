/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
         if (list1 == null) return list2;
        if (list2 == null) return list1;
        
        ListNode handler;
        if(list1.val < list2.val) {
            handler = list1;
            handler.next = mergeTwoLists(list1.next, list2);
        } else {
            handler = list2;
            handler.next = mergeTwoLists(list1, list2.next);
        }
        
        return handler;
    }
}
