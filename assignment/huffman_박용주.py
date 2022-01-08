import copy
class Node:
    def __init__(self, char, num):
        self.right = None
        self.left = None
        self.data = char
        self.freq = num
        self.huff = []
        
class Huffman:
    def __init__(self, char, num):
        self.root = None
        self.char = [char for _, char in sorted(zip(num, char))]
        self.num = [num for num, _ in sorted(zip(num, char))]
        self.nodes = []
    
    def selectTwo(self, num):
        minVal = num[0] + num[1]
        minFir = 0
        minSec = 1
        
        for i in range(len(num)-1):
            if num[i] + num[i+1] < minVal:
                minVal = num[i] + num[i+1]
                minFir = i
                minSec = i+1
        
        return minFir, minSec
    
    def createTree(self):
        print("Huffman coding tree")
        
        # step 0. sort char and num
        print(self.num)
        
        # step 1. create terminal node
        for i in range(len(self.char)):
            tmp = Node(self.char[i], self.num[i])
            self.nodes.append(tmp)
         
        # step 2. create parent node
        while True:
            try:
                if len(self.num) <= 1:
                    break
                
                # 인접한 두 개를 더하는 것 중에 제일 작은 노드를 찾는다. 
                first, second = self.selectTwo(self.num)
                # 단말 노드를 합해 부모 노드를 만든다
                tmp = Node('', self.nodes[first].freq+self.nodes[second].freq)
                tmp.left = self.nodes[first]
                tmp.right = self.nodes[second]
                 
                # node 리스트, num 리스트를 재조정해준다
                self.nodes.pop(first)
                self.nodes.pop(second-1)
                self.num.pop(first)
                self.num.pop(second-1)
                self.nodes.insert(first, tmp)
                self.num.insert(first, tmp.freq)
                
                # 현 상태 출력
                print(self.num)
            except:
                pass
        self.root = tmp
        
    def createCode(self, root, code):
        if root.left == None and root.right == None:
            root.huff = code
            print(root.data, root.huff)
            return
        else:
            root.huff = code
            left = copy.deepcopy(code)
            left.append('0')
            right = copy.deepcopy(code)
            right.append('1')
            self.createCode(root.left, left)
            self.createCode(root.right, right)
        # root 노드에서 시작한다.   
        # 탐색하면서 왼족에는 0, 오른족에는 1을 append 해준다.     
          
    def codes(self):
        print("Huffman codes")      
        self.createCode(self.root, [])  

# character
char = ['w', 'f', 'r', 'm', 'e', 'd', 'o', 't', 'i', 'a', 'n','\' \'']
# frequency
num =  [3, 3, 2, 2, 6, 3, 3, 2, 1, 1, 2, 1]

# character
char = ['a', 'b', 'c', 'd', 'e', 'f']
# frequency
num =  [6,5,4,3,2,1]

h = Huffman(char, num)
print()
h.createTree()
print()
h.codes()