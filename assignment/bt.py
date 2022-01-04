class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        
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
            self.printBT(tree.left)
            try:
                print("%d" % tree.data)
            except:
                print("%s" % tree.data)
            self.printBT(tree.right)
    
    
    def nodeDepth(self, node, d):
        if node:
            self.nodeDepth(node.left, d+1)
            try:
                print("%d %d" % (node.data, d))
            except:
                print("%s %d" % (node.data, d))
            self.nodeDepth(node.right, d+1)   
             
    def nodeCalculate(self, node):
        if node.left or node.right:
            return max(self.nodeCalculate(node.left), self.nodeCalculate(node.right)) + 1
        else:
            return 0
    
    def nodeHeight(self, node):
        if node:
            self.nodeHeight(node.left)
            try:
                print("%d" % (node.data), end=' ')
            except:
                print("%s" % (node.data), end =' ')   
            print("%d" % self.nodeCalculate(node)) 
            self.nodeHeight(node.right) 
        else:
            return 0  
            
    def treeDepth(self, node):
        if node:
            self.nodeHeight(node.left)
            try:
                print("%d" % (node.data), end=' ')
            except:
                print("%s" % (node.data), end =' ')  
            print("%d" % self.nodeCalculate(node))
            self.nodeHeight(node.right)
        else:
            return 0
        
    def treeHeight(self):
        pass
            
c = BinaryTree()
c.printBT(c.root)
print('DDDDDDD')
c.nodeDepth(c.root, 0)
print('HHHHHH')
c.nodeHeight(c.root )