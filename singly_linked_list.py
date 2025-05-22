class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        last = self.head

        while last.next:
            last = last.next
        
        last.next = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")
    
    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_after(self,prev_node, new_data):
        if prev_node is None:
            print("The given previous node cannot be None.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def delete_from_beginning(self):

        if self.head is None:
            return
        
        temp = self.head
        self.head = temp.next
        temp = None
    
    def delete_from_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        
        second_last.next = None
    
    def delete_by_key(self, key):
        temp = self.head

        if temp is not None and temp.data == key:

            self.head = temp.next

            temp = None
            return
        
        prev = None

        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next
        
        if temp is None:
            return
        
        prev.next = temp.next

        temp = None

llist = LinkedList()
llist.insert_at_beginning(10)
llist.append(20)
llist.insert_after(llist.head, 15)
llist.print_list()
llist.delete_from_beginning()
llist.print_list()
llist.delete_from_end()
llist.print_list