def tbt_inorder(tree):
    temp = tree
    while True:
        temp = successor(temp)
        if temp == tree: break
        print("%3c" % temp.data)

def successor(tree):
    temp = tree.right
    if not tree.right_thread:
        while not temp.left_thread:
            temp = temp.left
    return tmp

class Heap:
    def __init__(self, size):
        self.size = size
        self.heap = [None]*size
        self.count = 0
    def isEmpty(self):
        # element가 1개 들어가는 것이 empty
        # [0]에는 None이 들어가기 때문이다. 
        return self.count == 1 # 0 is dummy
    def isFull(self):
        return self.size - 1 == self.count
    def add_heap(self, item):
        if self.isFull(): return
        self.count += 1
        i = self.count
        # i가 첫 노드가 아니며, 
        # item이 i의 부모보다 클 때
        while i != 1 and item > self.heap[i//2]:
            self.heap[i] = self.head[i//2] # 부모랑 자식의 자리를 바꿔준다
            i //= 2 # 위에 거랑 다시 비교해준다
        self.heap[i] = item
        print("%2d" %item, end='')
        print(self.heap)