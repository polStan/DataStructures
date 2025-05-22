class SinglyNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)
    def display(head):
        curr = head
        elements = []
        while curr:
            elements.append(str(curr.value))
            curr = curr.next
        print('-->'.join(elements))


    

Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)
Head = Head.display()
Head.next = A
A.next = B
B.next = C

print(Head)

curr = Head
while curr:
    print(curr)
    curr = curr.next

def display(head, value):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    print('-->'.join(elements))

display(Head)