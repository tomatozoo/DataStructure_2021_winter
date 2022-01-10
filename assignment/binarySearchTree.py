class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.tree = None
    def rBST(self, root, key):
        if not root:
            # 요소를 찾지 못한 경우
            return None
        if key == root.data:
            return root
        if key < root.data:
            return self.rBST(root.left)
        else:
            return self.rBST(root.right)
    def iBST(self, root, key):
        while root:
            if key == root.data:
                return root
            elif key < root.data:
                root = root.left
            else:
                root = root.right
        return None
    def insert(self, item):
        node = Node(item)
        # 빈 트리면, self.tree에 node를 할당해준다. 
        if not self.tree:
            self.tree = node
        else:
            # 현재 노드
            temp = self.tree
            prev = None
            while True:
                prev = temp
                # 상위 노드
                # 왼쪽 서브 트리로 이동
                if item < prev.data:
                    prev = prev.left              
                # 오른쪽 서브 트리로 이동
                elif item > prev.data:
                    prev = prev.right                   
                # 중복 노드
                else:
                    print("중복 노드입니다")
                    return
    def find_delete(self, item):
        self.tree = self.delete_node(self.tree, item)
    def delete_node(self, node, item):
        if node is None: return None
        if node.data > item:
            node.left = self.delete_node(node.left, item)
            return node
        elif node.data < item:
            node.right = self.delete_node(node.right, item)
            return node
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            elif node.left is None and node.right is None:
                return None
            else:
                left_max = self.find_max(node.left)
                node.data = left_max.data
                node.left = self.delete_node(node.left, left_max.data)
                return node
    def find_max(self, root):
        if not root: return None
        node = root
        prev = node
        while node.right:
            prev = node
            node = node.right
        return node