class Node:
    def __init__(self, data=None):
        self.data = data  # Element of the node
        self.next = None  # The next node in the list None

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # The head of the list
    
    # Method to insert at the beginning
    def insert_at_beginning(self,data):
        new_node = Node(data) # Creating the new node with the data
        new_node.next = self.head # new_nodes next is updated to point to the head
        self.head = new_node # Then head is updated to point to the new node

    # Method to insert at end
    def insert_at_end(self, data):
        new_node = Node(data) # A new node with the data is created
        if not self.head: # If head is not none
            self.head = new_node # head is updated to point to the new node
        else: # Else statement when head is none
            current = self.head # the current pointer is updated to point to the head
            while current.next: # While statement to say if the next value exists
                current = current.next # current is updated to point to the next node
            current.next = new_node # then next of current node is updated to point to the new node

    # Method to insert at middle
    def insert_at_middle(self, data):
        if self.head == None: #check if the linked list is empty
            self.head = Node(data)
        else:
            # creates a new node
            newNode = Node(data)
            current = self.head
            length = 0
            # calculate the length of the linked list
            while current is not None:
                current = current.next
                length += 1
            # 'count' the number of node after which the new node has to be inserted
            if length % 2 == 0 :
                count = length // 2
            else:
                count = (length + 1) // 2
 
            current = self.head
            # move current to the node after which the new node has to inserted
            while count > 1 :
                current = current.next
                count -= 1
            # insert the 'newNode' and adjust links accordingly
            newNode.next = current.next
            current.next = newNode

    # Method to delete a node by value
    def delete_by_value(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next  # Move the head if the node to delete is the first one
            current = None
            return
        prev = None

        while current and current.data != data:
            prev = current
            current = current.next
        
        if current is None:
            print(f"Node with value {data} not found")
            return
        
        prev.next = current.next
        current = None
    
    # Method to search for a node by value
    def search_by_values(self, data):
        current = self.head
        position = 1  # Start at position 1
        while current:
            if current.data == data:#checking if the current value is equal to the given data
                return position  # return the position of the data
            current = current.next
            position += 1
        return None  # if data is not found, return None

    # Reversing  the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current: 
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def getLen(self):
        temp = self.head
        len = 0
        while temp != None:
            len = len + 1
            temp = temp.next
        return len
 
    def printMiddle(self):
        if self.head != None:
            # find length
            len = self.getLen()
            temp = self.head
 
            # traverse till reaching half of length
            midIdx = len // 2
            while midIdx != 0:
                temp = temp.next
                midIdx = midIdx - 1
        return temp.data
    
    #function to print the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Creating an empty linked list
sll = SinglyLinkedList()

# Inserting values at the beginning, end, and middle
print("Inserting values at beginning, end, and middle:")

print("List after inserting 10 in beginning:")
sll.insert_at_beginning(10)

print("List after inserting 20 in beginning:")
sll.insert_at_beginning(20)
sll.print_list()

print("List after inserting 30 in beginning:")
sll.insert_at_beginning(30)
sll.print_list()

print("List after inserting 40 at end:")
sll.insert_at_end(40)
sll.print_list()

print("List after inserting 50 at end:")
sll.insert_at_end(50)
sll.print_list()

print("List after inserting 60 at end:")
sll.insert_at_end(60)
sll.print_list()


print("List after inserting 70 in the middle:")
sll.insert_at_middle(70)
sll.print_list()

print("List after inserting 80 in the middle:")
sll.insert_at_middle(80)
sll.print_list()

# Delete a node and display the list
print("\nDeleting node with value 10:")
sll.delete_by_value(10)
sll.print_list()

print("\nDeleting node with value 4:")
sll.delete_by_value(4)
sll.print_list()

# Search for values and print their positions
print("\nSearching for values in the list:")
index = sll.search_by_values(12)
print(index)
if index is not None:
    print(f"Position of 12: {index}")
else:
    print("Element is not found.")

index = sll.search_by_values(2)
if index is not None:
    print(f"Position of 2: {index}")
else:
    print("Element is not found.")

print("\nDisplaying the list and its length:")
sll.print_list()
print("Length of list:", sll.getLen())

# Reverse the list and display it
print("\nReversing the list:")
sll.reverse()
sll.print_list()

# Find and return the middle element
print("\nFinding the middle element:")
middle = sll.printMiddle()
print(f"The middle element is: {middle}")

sll.print_list()






