# fibonacci
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-2)+fibonacci(num-1)

# prime number # num보다 작은 prime # 출력
# 10
# 1 3 5 7
# 이것보다 작은 소수로 나누어 떨어지지 않으면 소수임
def prime(num):
    primeList = [2]
    for i in range(2, num+1):
        for j in primeList:
            if i % j == 0:
                break
        else:
            primeList.append(i)
    return primeList
print("PRIME")
print(prime(15))
print("PRIME")

# fraction
class fraction:
    def __init__(self, num, dim):
        self.num = num
        self.dim = dim
        
    # __str__
    def __str__(self):
        return '{0}/{1}'.format(self.num, self.dim)
    
    # __add__
    def __add__(self, frac):
        new = fraction(1,1)
        new.num = self.num * frac.dim + self.dim * frac.num
        new.dim = self.dim * frac.dim
        common = self.gcd(new.num, new.dim)
        new.num //= common
        new.dim //= common
        return new
    
    # multiply
    def multiply(self, frac):
        new = fraction(1,1)
        new.num = self.num * frac.num
        new.dim = self.dim * frac.dim
        common = self.gcd(new.num, new.dim)
        new.num //= common
        new.dim //= common        
        return new
    
    # gcd
    def gcd(self, a, b):
        if b <= 1:
            return a
        else:
            return self.gcd(b, a%b)

f1 = fraction(1, 3)
f2 = fraction(2, 4)

print(f1)
print(f2)
print(f1+f2)  
print(f1.multiply(f2))
    
# bowling game
score1 = [(8,0), (4,3), (4,6), (2,6), (10,0), (9,0), (10,0), (8,2), (10,0),(10,10)]
score2 = [(10,0), (10,0), (10,0),(10,0), (10,0), (10,0),(10,0), (10,0), (10,0),(10,0),(10,10)]

def bowling(score):
    total = i = 0
    frame = []
    for first, second in score:
        f_total = first+second
        if i != 9:
            next_first, next_second = score[i+1]
        if first == 10:
            result = 'STRIKE'
            f_total += next_first + next_second
            if i < 8 and next_first == 10:
                next_next_first, next_next_second = score[i+2]
                f_total += next_next_first
        elif (first+second)==10:
            result = 'SPARE'
            f_total += next_first
        else: result = 'NONE'
        total += f_total
        frame.append((f_total, result))
        i += 1
        if i == 10: break
    print(frame)
    print("Total = ", total)
    print()

bowling(score1)
bowling(score2)

# factorial
def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return factorial(num-1)
    
# gcd
def gcd(self, a, b):
        if b <= 1:
            return a
        else:
            return self.gcd(b, a%b)
        
        
# binary search

def bSearch(lst, ans, start, end):
    mid = (start + end) // 2
    
    if start <= end:
        if lst[mid] == ans:
            print(mid)
            return mid
            
        elif lst[mid] > ans: 
            bSearch(lst, ans, start, mid)
        else:
            bSearch(lst, ans, mid, end)
            
    else:
        return -1
    
print("BSEARCH")
lst = [1,2,3,4,5,6,7,8,9,10] # 14
bSearch(lst, 9, 0,len(lst)-1)
print("BSEARCH")

# fibo1, fibo2

# htower(n,a,b)
def htower(n, a, b):
    if n == 1:
        print(f"{a} -> {b}")
    else:
        c = 6 - a - b
        htower(n-1, a, c)
        print(f"{a} -> {b}")
        htower(n-1, c, b)
        
htower(3, 1, 3)

# permutation
def permutation(fr, to): # 3P2
    pass

# N Queens Problem

    # __init__
    
    
    # put_queen
    
    # check_pos
    
    # show_board
    

# stack
class stack:
    # __init__
    def __init__(self):
        self.stk = []
        self.top = 0
        self.cnt = 0
    # empty
    def empty(self):
        return len(self.stk) == 0
    # size
    def size(self):
        return len(self.stk)
    # push
    def push(self, data):
        self.stk.append(data)
    # pop
    def pop(self):
        if self.empty():
            print("EMPTY STACK")
        else:
            return self.stk.pop()
    # view
    def view(self):
        print(self.stk)
    # peek
    def peek(self):
        print(self.stk[len(self.stk)-1])
        return self.stk[len(self.stk)-1]

exSTK = stack()
exSTK.push(0)
exSTK.push(1)
exSTK.push(2)
exSTK.push(3)
print(exSTK.pop())
print(exSTK.pop())
print(exSTK.pop())

# queue
class queue:
    # __init__
    def __init__(self):
        self.que = []
    # empty
    def empty(self):
        return len(self.que)==0   
    # size
    def size(self):
        return len(self.que)
    # enqueue
    def enqueue(self,data):
        self.que.append(data)  
    # dequeue
    def dequeue(self):
        if self.empty():
            print("EMPTY QUEUE")
        else:
            return self.que.pop(0)                
    # view
    def view(self):
        if self.empty:
            print("EMPTY QUEUE")    
        else:
            print(self.que)     
         
    # peek
    def peek(self):
        if self.empty:
            print("EMPTY QUEUE")      
        else:
            return self.que[0]
         
exQUE = queue()
exQUE.enqueue(0)
exQUE.enqueue(1)
exQUE.enqueue(2)
exQUE.enqueue(3)
print(exQUE.dequeue())
print(exQUE.dequeue())
print(exQUE.dequeue())
    
# CQueue
class cQueue:
    pass
    # __init__
    
    # empty
    
    # full
    
    # view
    
    # push
    
    # pop
    



### left

# Circular Queue

class CQueue:
    # __init__
    def __init__(self, size):
        self.size = size
        self.cq = [None] * self.size 
        # [front]
        # [rear]
        # [none none none none none]
        self.front = 0
        self.rear = 0
        self.count = 0
    # empty
    def empty(self):
        return self.front == self.rear
    # full
    def full(self):
        return self.front == (self.rear + 1) % self.size
    # view
    def view(self):
        return self.cq
    # push
    def push(self, data):
        if self.full():
            print("FULL CQUEUE")
        else:
            
            self.cq[self.rear] = data
            self.rear += 1
    # pop
    def pop(self):
        if self.empty():
            print("EMPTY CQUEUE")
        else:
            data = self.cq[self.front]
            self.cq[self.front] = None
            self.front += 1
            return data

print()
que = CQueue(6)
que.push(1)
que.push(1)
que.push(2)
que.push(3)
que.push(4)
que.push(5)
que.push(6)
print()
print(que.pop())
print(que.pop())
print(que.pop())
print(que.pop())

# bowling game

# N Queens Problem
def NQueens(N):
    pass

class NQeens:
    def __init__(self, size): 
        self.size = size
        self.col = [None] * self.size
        
    def put_queen(self, row):
        self.col[row]
                    
    def check_pos(self, rows, col):
        pass
            
    def show_board(self):
        pass
