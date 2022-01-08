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
        
        temp = Node('H')
        self.root = temp
        temp = Node('E')
        self.root.left = temp   
        temp = Node('D')
        self.root.right = temp        
        temp = Node('L')
        self.root.left.left = temp        
        temp = Node('O')
        self.root.left.right = temp        
        temp = Node('A')
        self.root.right.right = temp        
        temp = Node('T')
        self.root.right.right.left = temp        
        temp = Node('M')
        self.root.right.right.right = temp        
        temp = Node('P')
        self.root.left.left.left = temp              
    
    # node 탐색 후 depth 계산
    def depth_node(self, root, item):
        self.inorderSearch(root, item, 0)
    def inorderSearch(self, root, item, depth):
        if root:
            if root.data == item:
                print(root.data, depth)
                return 
            self.inorderSearch(root.left, item, depth+1)
            self.inorderSearch(root.right, item, depth+1)
    
    # node 탐색 후 height 계산
    def height_node(self, root, item):
        # find_node
        if root:
            if root.data == item:
                print(root.data, end=' ')
                print(self.cal_height(root))
                return
            self.height_node(root.left, item)
            self.height_node(root.right, item)
    def cal_height(self, root):
        left = 0
        right = 0
        if root:
            if root.left:
                left = self.cal_height(root.left)
            if root.right:
                right = self.cal_height(root.right)
            if root.left or root.right:
                return max(left, right) +1
            else:
                return 0
            

           

    # depth
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
            
    # height
    def height(self, root):
        # 결국 root의 depth를 찾는다
        self.findheight(root, 0) 
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
        
# create tree            
c = BinaryTree()
# tree height
c.height(c.root)
# node height
for i in ['H', 'E', 'L', 'P', 'O', 'D', 'A', 'T', 'M']:
    c.height_node(c.root, i)
# tree depth
c.depth(c.root)
# node depth
for i in ['H', 'E', 'L', 'P', 'O', 'D', 'A', 'T', 'M']:
    c.depth_node(c.root, i)