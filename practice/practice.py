# fibonacci
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-2)+fibonacci(num-1)

# prime number
def prime():
    pass

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

# factorial

# gcd

# binary search

# fibo1, fibo2

# htower(n,a,b)

# permutation

# N Queens Problem

    # __init__
    
    
    # put_queen
    
    # check_pos
    
    # show_board
    

# stack

    # __init__
    
    # empty
    
    # size
    
    # push
    
    # pop
    
    # view
    
    # peek
    
# queue

    # __init__
    
    # empty
    
    # size
    
    # enqueue
    
    # dequeue
    
    # view
    
    # peek

# CQueue

    # __init__
    
    # empty
    
    # full
    
    # view
    
    # push
    
    # pop
    
    