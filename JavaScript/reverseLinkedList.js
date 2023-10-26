/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 * 
 * Good test cases
 * 
 * Case 1
 * head = [1,2,3,4,5]
 * 
 * Case 2
 * head = [1,2]
 * 
 * Case 3
 * head = []
 */

function reverseList(head) {
    let previous = null
    let current = head

    while (current) {
        const nextNode = current.next
        current.next = previous
        previous = current
        current = nextNode
    }

    return previous
};