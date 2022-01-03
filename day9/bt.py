def postorder(tree):
    if tree:
        postorder(tree.left)
        postorder(tree.right)
        print("%d" % tree.data)

def inorder(tree):
    if tree:
        inorder(tree.left)
        print("%d" % tree.data)
        inorder(tree.right)

def preorder(tree):
    if tree:
        print("%d" % tree.data)
        preorder(tree.left)
        preorder(tree.right)

def iterative_inorder(tree):
    node = tree
    while True:
        while node:
            push(node)
            node = node.left
        node = pop()
        if not node: break
        print("%d" %node.data)
        node = node.right
def levelorder(self, node):
    if not node: return
    self.add(node)
    while True:
        node = self.delete()
        if node:
            print(node.data, end=' ')
            if node.left:
                self.add(node.left)
            if node.right:
                self.add(node.right)
        else: break

def copyTree(tree):
    if tree:
        temp = None(tree.data)
        temp.left = copyTree(tree.left)
        temp.right = copyTree(tree.right)
        return temp
    return None

class Node:
    def __init__(self, data):
        self.data = data
        self.value = None
        self.left = None
        self.right = None
    def postorder(self, tree):
        pass
    def eval_tree(self, node):
        if node:
            self.eval_Tree(node.left)
            self.eval_tree(node.right)
            
            if node.data == '+':
                node.value = node.left.value + node.right.value
            elif node.data == '-':
                node.value = node.left.value-node.right.value
            elif node.data == '*':
                node.value = node.left.value * node.right.value
            elif node.data == '/':
                node.value = node.left.value/node.right.value
            else:
                node.value = int(node.data)
                print(node.value, end=' ')
                
class Solution:
    def dfs(self,root,res) :
        if root : 
            self.dfs(root.left,res)
            self.dfs(root.right,res)
            res.append(root.val)
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res= []
        self.dfs(root,res)
        return res

def postorder(tree):
    if tree:
        postorder(tree.left)
        postorder(tree.right)
        print("%d" % tree.data)