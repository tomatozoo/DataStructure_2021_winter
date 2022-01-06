def rBST(root, key):
    if not root: return None
    if key == root.data: return root
    if key < root.data:
        return rBST(root.left, key)
    return rBST(root.right, key)

def iBST(root, key):
    while root:
        if key==root.data: return root
        if key < root.data:
            root = root.left
        else:
            root = root.right
    return None

def insert(self, item):
    node = Node(item)
    if not self.tree:
        self.tree = node
    else:
        temp = self.tree
        # 상위 노드
        prev = None
        while True:
            # 직전 노드 저장해두기
            prev = temp
            # item 현재 삽입하려는 item이
            # prev보다 작다면, 
            # left로 내려가기
            if item < prev.data:
                temp = temp.left
                if not temp:
                    # 만약에 left 값이 비어있다면, 
                    # 노드를 넣어준다 :)
                    prev.left = node
                    return
                    # 비어있지 않다면 다시 내려가주어야 한다. 
            # right로 내려가기
            elif item > prev.data:
                temp = temp.right
                if not temp:
                    # 만약에 right 값이 비어있다면, 
                    # 노드를 넣어준다 :)
                    prev.right = node
                    return
            else: return

def find_delete(self, item):
    # item을 삭제하여라
    # 재귀 함수 작동을 위함
    self.tree = self.delete_node(self.tree, item)
    
def delete_node(self, node, item):
    if node is None: return None
    if node.data > item:
        # 탐색을 왼쪽 subtree로 이어간다
        node.left = self.delete_node(node.left, item)
        return node
    elif node.data < item:
        # 탐색을 오른쪽 subtree로 이어간다
        node.right = self.delete_node(node.right, item)
        return node
    else: # 실제로 삭제하는 경우
        if node.left is None: # 단말 노드이거나 one child인 경우
            return node.right # None이거나, right subtree를 주면 된다. 
        elif node.right is None: # 단말 노드이거나 one child인 경우
            return node.left # None이거나, left subtree를 주면 된다.
        elif node.left is None and node.right is None:
            return None
        else:
            # two child
            left_max = self.find_max(node.left) # left subtree의 max를 임의로 정한다. 
            node.data = left_max.data
            node.left = self.delete_node(node.left, left_max.data)
            return node

def find_max(self, root):
    # BST 이므로 최댓값은 최대한 우측으로
    # 최솟값은 최대한 좌측으로 이동해주면 된다!
    if not root: return None
    node = root
    while node.right:
        node = node.right
    return node