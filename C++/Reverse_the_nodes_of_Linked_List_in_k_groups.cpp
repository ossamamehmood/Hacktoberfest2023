class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head, k):
    """Reverses the nodes of a linked list k at a time, and returns the modified list.

    Args:
        head: The head of the linked list.
        k: The number of nodes to reverse.

    Returns:
        The reversed linked list.
    """
    # Function to reverse a sub-list from start to end
    def reverse_sublist(start, end):
        prev, curr = None, start
        while curr != end:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    # Initialize variables
    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy

    while True:
        group_start = prev_group_end.next
        group_end = group_start

        # Check if there are at least k nodes in the group
        for i in range(k):
            if not group_end:
                return dummy.next
            group_end = group_end.next

        # Reverse the current group
        prev_group_end.next = reverse_sublist(group_start, group_end)
        group_start.next = group_end

        # Update pointers for the next iteration
        prev_group_end = group_start

    return dummy.next
