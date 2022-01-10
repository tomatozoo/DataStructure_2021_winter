class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.treeDepth = 0
        self.treeHeight = 0
        
        temp = Node('-')
        self.root = temp
        
        temp = Node('+')
        self.root.left = temp
        
        temp = Node('/')
        self.root.right = temp
        
        temp = Node('*')
        self.root.left.left = temp
        
        temp = Node('C')
        self.root.left.right = temp
        
        temp = Node('D')
        self.root.right.left = temp
        
        temp = Node('E')
        self.root.right.right = temp
        
        temp = Node('A')
        self.root.left.left.left = temp
        
        temp = Node('B')
        self.root.left.left.right = temp
        
        
    def printBT(self, tree):
        if tree:
            try:
                print("%d" % tree.data)
            except:
                print("%s" % tree.data)
            self.printBT(tree.left)
            self.printBT(tree.right)
    
    # 탐색
    def inorderSearch(self, node, item):
        if node:
            if node.data == item:
                return node
        return None
    
    def depth_node(self, node, item):
        if node:
            try:
                print("%d %d" % (node.data, item))
            except:
                print("%s %d" % (node.data, item))
            self.depth_node(node.left, item+1)
            self.depth_node(node.right, item+1)   
        else:
            return -1
             
    def nodeCalculate(self, node):
        if node.left or node.right:
            return max(self.nodeCalculate(node.left), self.nodeCalculate(node.right)) + 1
        else:
            return 0
    
    # 탐색
    def height_node(self, node, item):
        if node:
            try:
                print("%d" % (node.data), end=' ')
            except:
                print("%s" % (node.data), end =' ')   
            print("%d" % self.nodeCalculate(node)) 
            self.height_node(node.left, item)
            self.height_node(node.right, item) 
        else:
            return 0  

    def depth(self, root):
        self.finddepth(root, 0)
        print(f'tree depth : {self.treeDepth}')
        
    def finddepth(self, root, depth):
        # return 조건
        if not root:
            return 0
        else:
            if self.treeDepth < depth:
                self.treeDepth = depth
            self.finddepth(root.left, depth+1)
            self.finddepth(root.right, depth+1)
        
    def height(self, root):
        self.findheight(self.root, 0) # 결국 root의 depth를 찾는다
        print(f'tree height : {self.treeHeight}')
        return 0 
    
    def findheight(self, root, height):
        if root:
            if self.treeHeight < height:
                self.treeHeight = height
            self.findheight(root.left, height+1)
            self.findheight(root.right, height+1) 
        else:
            return 0  
            
c = BinaryTree()
c.printBT(c.root)
print('DDDDDDD')
c.depth_node(c.root, 0)
print('HHHHHH')
c.height_node(c.root, 0)
print("TDTDTDTD")
c.depth(c.root)
print("HHHHDDDD")
c.height(c.root)


class BinaryTree:
    def __init__(self):
        self.root = None
        self.treeDepth = 0
        self.treeHeight = 0
        
        temp = Node('-')
        self.root = temp
        
        temp = Node('+')
        self.root.left = temp
        
        temp = Node('/')
        self.root.right = temp
        
        temp = Node('*')
        self.root.left.left = temp
        
        temp = Node('C')
        self.root.left.right = temp
        
        temp = Node('D')
        self.root.right.left = temp
        
        temp = Node('E')
        self.root.right.right = temp
        
        temp = Node('A')
        self.root.left.left.left = temp
        
        temp = Node('B')
        self.root.left.left.right = temp
        
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
    def postorder(self, node):
        if node:
            self.inorder(node.left)
            self.inorder(node.right)   
            print(node.data) 
    def preorder(self, node):
        if node:
            print(node.data) 
            self.inorder(node.left)
            self.inorder(node.right) 
            
    def iterative_inorder(self, node):
        stack = []
        while True:
            while node:
                stack.append(node)
                node = node.left
            try:
                node = stack.pop()
            except:
                break
            print(node.data)
            node = node.right
    def level_order(self, node):
        queue = [] # FIFO
        queue.insert(0, node)
        while queue:
            tmp = queue.pop(0)
            print(tmp.data)
            if tmp.left:
                queue.insert(0, tmp.left)
            if tmp.right:
                queue.insert(0, tmp.right)
    def copyTree(self, tree):
        if tree:
            node = Node(tree.data)
            node.left = self.copyTree(tree.left)
            node.right = self.copyTree(tree.right)
            return node

        
                
            

print("traverse")
c = BinaryTree()
print("inorder")
c.inorder(c.root)
print("postorder")
c.postorder(c.root)
print("preorder")
c.preorder(c.root)
print("iterative_inorder")
c.iterative_inorder(c.root)
print("level_order")
c.level_order(c.root)

class Node:
    def __init__(self, data):
        self.data = data
        self.value = None
        self.left = None
        self.right = None
class EvalTree: # inorder representation
    def __init__(self):
        self.root = None
        self.value = 0
        self.treeDepth = 0
        self.treeHeight = 0
        
        temp = Node('+')
        self.root = temp
        
        temp = Node('*')
        self.root.left = temp
        
        temp = Node('-')
        self.root.right = temp
        
        temp = Node('5')
        self.root.left.left = temp
        
        temp = Node('4')
        self.root.left.right = temp
        
        temp = Node('100')
        self.root.right.left = temp
        
        temp = Node('20')
        self.root.right.right = temp
                
    def eval_tree(self, node):
        if node:
            self.eval_tree(node.left)
            self.eval_tree(node.right)
            if node.data == '+':
                node.value = node.left.value + node.right.value
            elif node.data == '-':
                node.value = node.left.value - node.right.value
            elif node.data == '*':
                node.value = node.left.value * node.right.value
            elif node.data == '/':
                node.value = node.left.value / node.right.value
            else:
                node.value = int(node.data)
                print(node.value, end = ' ')
        

c = EvalTree()
c.eval_tree(c.root)
print(c.root.value)

class TBT_Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.rightFlag = None
        self.leftFlag = None

class TBT:
    def __init__(self, data):
        self.root = None
        # create Tree
        self.root = TBT_Node('-')
        self.root.left = TBT_Node('A')
        self.root.left.left = TBT_Node('B')
        self.root.left.right = TBT_Node('C')
        self.root.left.left.left = TBT_Node('D')
        self.root.left.left.right = TBT_Node('E')
        self.root.left.right.left = TBT_Node('F')
        self.root.left.right.right = TBT_Node('G')
        self.root.left.left.left.left = TBT_Node('H')
        self.root.left.left.left.right = TBT_Node('I')
        
    def tbt_inorder(self, node):
        temp = node
        while True:
            # 다음 노드를 찾아 출력한다. 
            temp = self.successor(temp)
            if temp == node:
                break
            print("%3c " % temp.data)
            
    def successor(self, node):
        temp = node.right
        if not (temp.rightFlag or temp.leftFlag):
            while not temp.left_thread:
                temp = temp.left
        return temp
        
    def define(self, node):
        temp = self.node
        if temp.left:
            self.define(temp.left)
        else:
            # inorder predecessor
            pass
        if temp.right:
            self.define(temp.right)
        else:
            # inorder successor
            pass
        return
    
    def predecessor(self, node):
        temp = self.node.left
        if not temp:
            return self.root
        while temp:
            if not temp.right:
                return temp
            temp = temp.right
            
    def successor(self, node):
        l = self.node.left
        r = self.node.right
        if not (l or r):
            return self.root
        while l or r:
            pass

class Heap:
    def __init__(self, size):
        self.size = size
        self.heap = [None] * size
        self.count = 0
    def isEmpty(self):
        return self.count == 0
    def isFull(self):
        return self.count == self.size
    def add_heap(self, item):
        if self.isFull():
            return
        i = self.count
        self.count += 1

        # empty heap이 아니고, 
        # item이 부모 노드보다 큰 경우에는, 
        while i != 0 and item > self.heap[i//2]:
            # temp 자리에 부모 노드의 값을 저장해두고
            self.heap[i] = self.heap[i//2]
            # 다시 부모 노드와 부부모 노드를 비교하는 것을 반복한다. 
            i//=2
        # 마침에 부모 노드 >= 자식 노드의 관계가 성립한다면, 
        # i번째 item으로, item을 저장한다. 
        self.heap[i] = item
        print("%2d " % item, end=' ')
        print(self.heap)
        
    def del_heap(self):
        if self.count == 0:
            print("Empty heap")
            return
        # root를 제거한다. 
        item = self.heap[0]
        temp = self.heap[self.count]
        self.heap[self.count] = None
        self.count -= 1
        
        parent = 1
        child = 2
        # rebuilding heap
        while child <= self.count:
            if child < self.count and \
                self.heap[child] < self.heap[child+1]:
                    # child < parent
                    child += 1
            try:
                if temp >= self.heap[child]:
                    # 재구성 완료
                    break
            except:
                break
            # swap 이 필요한 경우
            self.heap[parent] = self.heap[child]
            parent = child
            child *= 2
        if self.count != 0:
            # 마지막 탐색 위치에 temp 저장
            self.heap[parent] = temp
        return item
    def heapSort(self):
        n = self.size - 1
        for i in range(n//2, 0, -1):
            self.makeheap(i, n)
        print(self.num)
        for i in range(n-1, 0, -1):
            self.swap(1, i+1)
            self.makeheap(1, i)
            print(self.num)
    def makeheap(self, root, n):
        temp = self.num[root]
        child = 2 * root
        while child <= n:
            if child < n and self.num[child] < self.num[child + 1]:
                child += 1
            if temp > self.num[child]:
                break
            else:
                self.num[child//2] = self.num[child]
                child * 2
        self.num[child//2] = temp
    
c = Heap(10)
c.heap = [None,20,15,14,10,2, None, None, None, None]
c.count = 5
c.add_heap(5)
c.del_heap()
print(c.heap)