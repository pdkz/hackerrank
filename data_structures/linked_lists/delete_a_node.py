#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteNode(llist, position):
    if not llist:
        return llist

    if position == 0:
        llist = llist.next
        return llist

    i = 0
    node = llist
    while node.next and i < position:
        if i == position - 1:
            node.next = node.next.next
            break
        node = node.next
        i += 1

    return llist
