# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def mergeLists(head1, head2):
    merged_linkedlist = SinglyLinkedListNode(0)
    head = merged_linkedlist
    
    node1 = head1
    node2 = head2
    
    while node1 and node2:
        if node1.data < node2.data:
            merged_linkedlist.next = node1
            node1 = node1.next
        else:
            merged_linkedlist.next = node2
            node2 = node2.next
        merged_linkedlist = merged_linkedlist.next
    
    if not node1:
        merged_linkedlist.next = node2
    if not node2:
        merged_linkedlist.next = node1
    return head.next
