class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, value):
    new_head = head

    if (new_head == None):
        return None

    if (head.val == value):
        new_head = head.next
        head.next = None

    current = new_head
    while (current.next != None):
        print(current.val)
        if (current.next.val == value):
            current.next = current.next.next
            current.next.next = None
        current = current.next

    return new_head

def insert_after(first, second):
    if (first.next == None):
        first.next = second
        return first
    else:
        second.next = first.next.next
        first.next = second

A = ListNode(7)
B = ListNode(3)
C = ListNode(4)
D = ListNode(7)
E = ListNode(9)
insert_after(A,B)
insert_after(B,C)
insert_after(C,D)
insert_after(D,E)

Z = removeElements(A, 7)
