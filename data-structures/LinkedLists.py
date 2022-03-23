# Node class for every element in linked list
class Node:                                
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:                          
    def __init__(self):
        self.head = None

link_list = LinkedList()
link_list.head = Node(20)
sec = Node(21)
third = Node(22)

link_list.head.next = sec
sec.next = third

current = link_list.head
while(current): 
    print(current.data)
    current = current.next