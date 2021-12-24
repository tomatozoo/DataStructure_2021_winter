def fact_r(n):
    if n==0: return 1
    else: return fact_r(n-1)*n

i=20
for n in range(1, i+1):
    print(n, '!=', fact_r(n))
    
    
def gcd(x, y):
    if y==0: return x
    else: return gcd(y, x%y)

num = [(128,12), (45,120)]

for x, y in num:
    print("gcd(%d,%d)=%d" % (x,y,gcd(x,y)))
    
    
def rbinsearch(lst, item, left, right):
    if left <= right:
        mid = (left + right) // 2
        if item == lst[mid]:
            return mid
        elif item < lst[mid]:
            return rbinsearch(lst, item, left, mid-1)
        else:
            return rbinsearch(lst, item, mid+1, right)

mylist = [5,8,9,11,13,17,23,32,45,52,60,72]
print(mylist)

for item in [60,9,10]:
    pos = rbinsearch(mylist,item,0,len(mylist)-1)
    print("position of", item, " = ", pos)
    
import time

def fibo1(n):
    global count1
    count1 += 1
    if n <= 1: 
        return n
    else:
        return fibo1(n-2)+fibo1(n-1)
"""
for num in [10,20,30,40]:
    count1 = 0
    time1 = time.time()
    print("fibo1", num, "=", fibo1(num))
    time2 = time.time()
    print("time1 = ", time2-time1)
    print("recursion1 = ", count1)"""

def fibo2(n):
    global count2
    count2 += 1
    if n<=1:
        return (0,n)
    else:
        (a,b) = fibo2(n-1)
        return (b,a+b) # 직전 수랑 같이 보내준다
# 중복 호출을 피할 수 있다
# 이러면, 10을 구하라고 했을 때 재귀 호출이 10번만 일어난다. 
# 9, 8, 7, 6.. 을 호출

for num in [10,20,30,40]:
    count2 = 0
    time1 = time.time()
    print("fibo2", num, "=", fibo2(num))
    time2 = time.time()
    print("time2 =", time2-time1)
    print("recursion2 = ", count2)
  

print(fibo2(10))


def htower(n, a, b):
    global count
    count += 1
    if n==1:
        print("Disc %d, moved from Pole (%d) to (%d)" % (n,a,b))
    else:
        c = 6-a-b # 1 + 2 + 3 = 6 # 비어있는 기둥
        htower(n-1,a,c)
        print("Disc %d, moved from Pole (%d) to (%d)" % (n,a,b))
        htower(n-1, c, b)
        
"""count = 0
n = int(input("Enter disc number:"))
htower(n, 1, 2)
print("# move for %d discs : %d" % (n, count))"""


def permutation(word, i, n):
    if i==n: print(word)
    else:
        for j in range(i, n+1):
            
            # L로 시작하는 그룹
            # A로 시작하는 그룹
            # N으로 시작하는 그룹
            # G로 시작하는 그룹
            
            word[i], word[j] = word[j], word[i]
            permutation(word, i+1, n)
            word[i], word[j] = word[j], word[i]

word = ['L', 'A', 'N', 'G']
permutation(word, 0,3)

class NQeens:
    
    def __init__(self, size): # 순열 문제와 같다. 
        self.size = size
        self.solutions = 0
        self.col = [-1] * size
        
    def put_queen(self, row):
        if row==self.size:
            self.show_board()
            self.solutions += 1
        else:
            for col in range(self.size):
                if self.check_pos(row, col):
                    self.col[row] = col
                    # queen을 놓음
                    self.put_queen(row+1)
                    
    def check_pos(self, rows, col):
        # 잡아먹는 queen이 있는지 check
        for i in range(rows):
            if self.col[i] == col or \
                self.col[i] - i == col - rows or \
                self.col[i] + i ==col + rows:
                    return False
        return True
            
    def show_board(self):
        for row in range(self.size):
            line = ""
            
            for column in range(self.size):
                if self.col[row] == column:
                    line += 'Q'
                else:
                    line += "+ "
            print(line)
        print()

N = 4
q = NQeens(N)
q.put_queen(0)
print(q.solutions, "solutions found")

class Stack:
    def __init__(self):
        self.stack = []
    def empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
    def push(self, item):
        self.stack.append(item)
        self.view()
    def pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            print("Stack empty")
    def view(self):
        print(self.stack)
    def peek(self):
        if not self.empty():
            return self.stack[self.size()-1]
        else:
            return None

s = Stack()
for item in [3,4,5,6,7,8]:
    s.push(item)
print("stack size", s.size())
print("top", s.peek())

for i in range(7):
    print(s.pop(), end=' ')
