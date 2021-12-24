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