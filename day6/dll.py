class Node:
    def __init__(self, data):
        self.data = data
        self.llink = None
        self.rlink = None
    def insert(self, prev, item): # append after prve
        if not self.head: return
        node = Node(item) # insert to the frot if not prev
        if not prev:
            node.rlink = self.head
            self.head = node
            return
        before = self.find(prev)
        if not before:
            print("No prev node")
            return
        else:
            node.rlink = before.rlink
            if before.rlink: before.rlink.llink = node
            before.rlink = node
            node.llink = before
            if not node.rlink: self.rear = node
            
    def delete(self, item):
        if not self.head:
            print("List Empty")
            return
        node = self.find(item)
        if not node:
            print("Not Found")
            return
        if node.llink:
            node.llink.rlink=node.rlink
            if node.rlink:
                node.rlink.llink = node.llink
            print("Node is deleted. prev exist")
        else:
            if self.head == node:
                print("head is deleted")
            self.head = node.rlink
            if node.rlink:
                node.rlink.llink = None
        if self.rear == node: 
            self.rear = node.llink
        del node
