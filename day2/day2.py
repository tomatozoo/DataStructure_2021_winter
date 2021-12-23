a = 2
b = a
print("a", a, id(a)) #a가 참조하는 literal의 주소
print("b", b, id(b))
b = b+1
print("a", a, id(a))
print("b", b, id(b))

A = [2, 3, 4]
A[1] = 5
B = A
print("A", A, id(A))
print("B", B, id(B)) # B가 A의 alias가 됨
B.append(7)
print("A", A, id(A))
print("B", B, id(B))

def f(a):
    a = 3 # a는 3을 가리킴
    print(a)
    return a

b = 2 # b는 2를 가리킴
f(b) # 받는 변수가 지정되지 않음
print(b) # b는 바뀌지 않음
b = f(b) # b가 reference하는 곳이 3으로 바뀜
print(b)

num = [i for i in range(100)]
num = list(range(100))
num = []
for i in range(100):
    num = num + [i]
    
import copy
A = [[2,3,4],5]
B = copy.copy(A)
B[0][1] = 'f'
B[1] = 7
print(A, id(A), id(A[0]), id(A[0][1]))
print(B, id(B), id(B[0]), id(B[0][1]))

import copy
A = [[2,3,4],5]
B = copy.deepcopy(A)
B[0][1] = 'f'
B[1] = 7
print(A, id(A), id(A[0]), id(A[0][1]))
print(B, id(B), id(B[0]), id(B[0][1]))

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

# polynomial ADT
A = [(2,100), (1,0)]

B = [(1,4), (10,3), (3,2), (1,0)]

D = []

def padd(a, b, d):
    while a and b:
        coef1, exp1 = a[0]
        coef2, exp2 = b[0]
        if exp1 > exp2:
            d.append(a.pop(0)) # 가장 앞 원소를 꺼낸다 # a.pop 은 가장 뒷 원소
        elif exp1 < exp2:
            d.append(b.pop(0))
        else:
            d.append(((coef1+coef2), exp1))
            a.pop(0)
            b.pop(0)
    for coef, exp in a:
        d.append((coef, exp))
    for coef, exp in b:
        d.append((coef, exp))

a = [(5,12), (-6, 8), (13,3)]
b = [(10,15), (4,8), (9,0)]
d = []

print("a=",a)
print("b=", b)
padd(a,b,d)
print("d=", d)