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

def poly_add(a,b,d):
    pass
def del_list(self):
    node = self.head
    while node:
        temp = node
        node = node.link
        del temp
    print("List is deleted")
    self.head = None
    
def concat(self, second):
    if not self.head:
        return second
    elif second:
        temp = self.head
        while temp.link:
            temp = temp.link 
        temp.link = second
    return self.head
# Time Complexity = O(n) (n= length of first)

def length_list(self):
    if not self.head: return 0
    count = 0
    temp = self.head
    while True:
        count += 1
        temp = temp.link
        if temp == self.head: break
    return count

def add_sort(self, item):
    node = Node(item)
    if not self.head:
        self.head = node
        self.tail = node
        node.link = self.head
        return
    temp = self.head
    prev = None
    while temp:
        if item > temp.data:
            prev = temp
            temp = temp.link
        elif item == temp.data:
            print("Duplicate item")
            return
        else:
            node.link = temp
            if prev:
                prev.link = node
            else:
                self.head = node
                self.tail.link = node
            return
        if temp == self.head: break
    node.link = self.head
    prev.link = node
    
def reverse(self):
    first = self.head
    second = third = None
    self.tail = self.head
    while first:
        third = second
        second = first
        first = first.link
        second.link = third
    self.head = second
    return 