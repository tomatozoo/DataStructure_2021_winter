def view(self):
    temp = self.head
    print("[", end=' ')
    while temp:
        print(temp.data, end=' ')
        temp = temp.link
    print("]", end=' ')
    if self.head:
        print("H=", self.head.data, "R=",self.rear.data)
    else:
        print("List is Empty")
        
def isEmpty(self):
    return not self.head
def peek_front(self):
    if not isEmpty():
        print("List Empty")
    else:
        return self.head.data
def add_front(self, item):
    node = Node(item)
    if not self.head:
        self.head = node
        self.tail = node
    else:
        node.link = self.head
        self.head = node
def pop_front(self):
    if not self.head:
        print("List Empty")
        return None
    else:
        temp= self.head
        self.head = self.head.link
        item = temp.data
        del temp
        return item
def add_rear(self, item):
    node = Node(item)
    if not self.head:
        self.head = node
        self.tail = node
    elif self.tail:
        self.tail.link = node
        self.tail = node

def pop_rear(self):
    if not self.head:
        print("List Empty")
        return None
    else:
        item = self.tail.data
        prev, temp = self.find(item)
        self.tail = prev
        if prev:
            prev.link = None
        else:
            self.head = None
        del temp
        return item
