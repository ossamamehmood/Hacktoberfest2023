package main

import (
    "fmt"
)

type ListNode struct {
    Val  int
    Next *ListNode
}

func reverseLinkedList(head *ListNode) *ListNode {
    var prev *ListNode
    current := head

    for current != nil {
        next := current.Next
        current.Next = prev
        prev = current
        current = next
    }

    return prev
}

func main() {
    // Create a sample linked list
    head := &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: nil}}}

    fmt.Println("Original Linked List:")
    printLinkedList(head)

    // Reverse the linked list
    newHead := reverseLinkedList(head)

    fmt.Println("Reversed Linked List:")
    printLinkedList(newHead)
}

func printLinkedList(head *ListNode) {
    current := head
    for current != nil {
        fmt.Printf("%d -> ", current.Val)
        current = current.Next
    }
    fmt.Println("nil")
}
