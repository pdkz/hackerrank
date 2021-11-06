def insertNodeAtPosition(llist, data, position):
    head = llist
    node = head

    if position == 0:
        new_node = SinglyLinkedListNode(data)
        new_node.next = head
        head = new_node
        return head

    i = 0
    while i < position:
        if i == position - 1:
            next_node = node.next
            new_node = SinglyLinkedListNode(data)
            node.next = new_node
            new_node.next = next_node
            break
        node = node.next
        i += 1
    return head
