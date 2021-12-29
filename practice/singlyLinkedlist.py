import random
class Node:
    def __init__(self, item):
        self.data = item
        self.link = None

class SLL:
    def __init__(self):
        self.head = None
        self.rear = None
        self.count = 0
    def isEmpty(self):
        return self.head == None
    def addFront(self, node):
        tmp = self.head
        self.head = node
        node.link = tmp
        if self.count == 0:
            self.rear = self.head
        self.count += 1
    def addRear(self, node):
        tmp = self.rear
        self.rear = node
        self.rear.link = tmp
        if self.count == 0:
            self.head = self.rear
        self.count += 1
    def delFind(self, node):
        tmp = self.head 
        while True:
            if tmp == None:
                print("No such node")
                break
            elif tmp.data == node:
                del tmp
            else:
                tmp = tmp.link
        self.count -= 1
    def popFront(self):
        tmp = self.head.data
        self.head = self.head.link
        self.count -= 1
        return tmp
    def popRear(self):
        tmp = self.rear.data
        del tmp
        self.count -= 1
        return tmp
    def delAll(self):
        while True:
            if self.head == None:
                break
            tmp = self.head
            self.head = self.head.link
            del tmp
        self.count = 0
    def view(self):
        tmp = self.head
        while True:
            if tmp == None:
                break
            print(tmp.data)
            tmp = tmp.link
    def length(self):
        return self.count
    def concat(self, to):
        if self.head == None:
            self.head = to.head
        else:
            self.rear.link = to.head
    def peekFront(self):
        return self.head.data
    def peekRear(self):
        return self.rear.data
    def reverse(self):
        first = self.head
        second = third = None
        while first:
            third = second
            second = first
            first = first.link
            second.link = third
        self.head = second
    def addSort(self, node):
        # 비어있는 경우
        if self.count == 0 or \
            node.data <= self.head.data:
            self.addFront(node)
        elif node.data >= self.rear.data:
            self.addRear(node)
        else:
            tmp = self.head
            while True:
                if node.data <= tmp.link.data:
                    save = tmp.link
                    tmp.link = node
                    node.link = save
                else:
                    tmp = tmp.link
        self.count += 1
    def print(self):
        tmp = self.head
        while True:
            if tmp == None:
                break
            else:
                print(tmp.data)
                tmp = tmp.link
s = SLL()
for i in range(10):
    tmp = Node(i*100)
    s.addFront(tmp)
    
    
s.reverse()
s.print()