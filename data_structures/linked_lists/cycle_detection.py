#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    slow = head
    fast = head
    
    if not slow or not fast:
        return 0

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return 1
    return 0
