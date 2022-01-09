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