class Node:
    def __init__(self, item):
        self.data = item
        self.link = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.rear = None
    def isEmpty(self):
        return not self.head # head가 None
    def add_sort(self, item):
        # 조건 : 이미 정렬된 linked list여야 한다. 
        # 작은 건 건너뛰고
        # 큰 거 에서는 멈춰야 한다. 
        node = Node(item)
        if not self.head: # empty list
            self.head = node
            self.rear = node
            return
        else:
            temp = self.head
            prev = None
            while temp:
                if item > temp.data:
                    prev = temp
                    temp = temp.link
                elif item == temp.data:
                    print("Duplicate item")
                    # 중복되는 경우 거부한다. 
                    return
                else:
                    # item < temp.data
                    # node를 찾음
                    node.link = temp
                    if prev: prev.link = node # 중간에 들어감
                    else: self.head = node # 가장 앞에 들어감
                    return
        # 너무 커서
        # 맨 뒤에 붙이는 경우이다
        prev.link = node
        self.tail = node

        node.data
        
    def del_find(self, item):
        if not self.head:
            print("List EMpty")
            return
        prev, node = self.find(item)
        if not node:
            print("Not Found")
            return
        if prev:
            prev.link = node.link
            print("Node is deleted")
        else:
            if self.head == node:
                print("Head is deleted")
                self.head = node.link
        if node == self.tail:
            self.tail = prev
        del node
    def find(self, item):
        if not self.head:
            return None, None 
        temp = self.head
        prev = None
        while temp:
            if temp.data == item:
                return prev.temp
            prev = temp
            temp = temp.link # temp = temp.next와 같다
        return None, None
    def view(self):
        temp = self.head
        print("[", end=' ')
        while temp:
            print(temp.data, end=' ')
            temp=temp.link
        print("]", end=' ')
        if self.head:
            print("H=", self.head.data, "R=", self.rear.data)
        else:
            print("List is Empty")
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.link
        return count
    

lst = SinglyLinkedList() # 객체
for item in range(10):
    lst.add_sort(item)
lst.view()
print("List length = ", lst.length())