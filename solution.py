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
        if (current.next != None):
            current = current.next

    return new_head

def insert_after(first, second):
    if (first.next == None):
        first.next = second
        return first
    else:
        second.next = first.next.next
        first.next = second

A = ListNode(1)
B = ListNode(2)
C = ListNode(6)
D = ListNode(3)
E = ListNode(4)
F = ListNode(5)
G = ListNode(6)
insert_after(A,B)
insert_after(B,C)
insert_after(C,D)
insert_after(D,E)
insert_after(E,F)
insert_after(F,G)


Z = removeElements(A, 6)
