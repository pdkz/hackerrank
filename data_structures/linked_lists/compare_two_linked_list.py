#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    node1 = llist1
    node2 = llist2
    
    while node1.next and node2.next:
        if node1.data != node2.data:
            # the sequence of data is not equal
            return 0
        node1 = node1.next
        node2 = node2.next
    
    if node1.next == None and node2.next == None:
        return 1
    return 0
