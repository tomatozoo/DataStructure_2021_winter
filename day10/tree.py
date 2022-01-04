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

def del_heap(self):
    if self.count == 0:
        print("empty heap")
        return
    item = self.heap[1]
    temp = self.hea[self.count]
    self.heap[self.count] = None
    self.count -= 1
    parent = 1
    child = 2
    
    while child <= self.count:
        if child < self.count and \
            self.heap[child] < self.heap[child+1]:
                child += 1
        if temp >= self.heap[child]: break
        self.heap[parent] = self.heap[child]
        parent = child
        child *= 2
    if self.count != 0:
        self.heap[parent] = temp
    return item

    def sort(self):
        n = self.size - 1
        for i in range(n//2, 0, -1):
            self.makeheap(i, n) # 초기 최대 힙
        print(self.num)
        for i in range(n-1, 0, -1):
            self.swap(1, i+1) # max 값을 마지막 원소와 교환
            self.makeheap(1, i) # 재정렬할 노드, 노드 수
            print(self.num)
    
    def makeheap(self, root, n):
        # 재정렬할 root, node 수
        temp = self.num[root]
        child = 2 * root # 왼쪽 자식 노드
        while child <= n:
            if child < n and self.num[child] < self.num[child+1]:
                child += 1
            if temp > self.num[child]: break
            # 부모와 자식 노드 중 큰 것과 비교 
            else:
                # 자식 노드를 부모 위치로 이동
                self.num[child//2] = self.num[child]
                # 한 레벨 낮춘다
                child *= 2
        self.num[child//2] = temp
        
