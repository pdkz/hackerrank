# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    if not head:
        return head
    
    node = head
    while node.next:
        node = node.next
    node.next = data

    return head
