class Node:
    def __init__(self, data):
        self.data = data
        self.rlink = None
        self.llink = None
    
class DLL:
    def __init__(self):
        self.head = None
        self.rear = None
        self.cnt = None
    def insert(self, item):
        tmp = Node(item)
        if self.head == None:
            self.head = tmp
        else:
            right = self.head.rlink
            self.head.rlink = tmp
            tmp.llink = self.head
            tmp.rlink = right
            
            
    def print(self):
        tmp = self.head
        while tmp != None:
            print(tmp.data)
            tmp = tmp.rlink

d = DLL()
d.insert(6)
d.insert(5)
d.insert(4)
d.print()