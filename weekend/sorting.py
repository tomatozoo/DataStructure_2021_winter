class SelectionSort:
    def __init__(self, num):
        self.lst = num
        self.n = 0
    def __str__(self):
        for i in self.lst:
            print("%2d " % i)
    def sort(self):
        start = 0
        while True:
            if start == len(self.lst)-1:
                # list에 최종적으로 추가하고
                break
            tmpMin = self.lst[start]
            tmpInd = 0
            if start == len(self.lst):
                # list에 최종적으로 추가하고
                break
            for i in range(start, len(self.lst)):
                # 최솟값(값, index)을 찾아.
                if tmpMin >= self.lst[i]:
                    tmpMin = self.lst[i]
                    tmpInd = i
            # start 위치와 swap
            self.lst[tmpInd] = self.lst[start]
            self.lst[start] = tmpMin
            start += 1

num = [31,9,10,23,49,15,11,7]
s = SelectionSort(num)
s.sort()
print(s.lst)

class BubbleSort:
    def __init__(self, num):
        self.lst = num
        self.n = 0
    def __str__(self):
        for i in self.lst:
            print("%2d " % i)
    def swap(self, a, b):
        tmp = self.lst[a]
        self.lst[a] = self.lst[b]
        self.lst[b] = tmp
    def sort(self):
        for i in range(len(self.lst)-1):
            for j in range(len(self.lst)-1):
                if self.lst[j] >= self.lst[j+1]:
                    self.swap(j, j+1)

num = [31,9,10,23,49,15,11,7]
s = BubbleSort(num)
s.sort()
print(s.lst)

class InsertionSort:
    def __init__(self, num):
        self.lst = num
    def __str__(self):
        for i in self.lst:
            print("%2d " % i)
    def sort(self):
        for i in range(1, len(self.lst)):
            d = 0
            tmp = self.lst[i]
            for j in range(0, i):
                if tmp <= self.lst[j]:
                    t = self.lst[i]
                    self.lst[i] = self.lst[j]
                    self.lst[j] = t
                    d = 1
                else:
                    continue
            
num = [31,9,10,23,49,15,11,7]
s = InsertionSort(num)
s.sort()
print(s.lst)

class shellSort:
    def __init__(self, num):
        self.lst = num
    def __str__(self):
        for i in self.lst:
            print("%2d " % i)
    def sort(self):
        gap = len(self.lst) // 2
        while True:
            if gap < 1:
                break
            for i in range(0, len(self.lst),gap):
                tmp = self.lst[i]
                for j in range(0, i, gap):
                    if tmp<= self.lst[j]:
                        t = self.lst[i]
                        self.lst[i] = self.lst[j]
                        self.lst[j] = t
            gap //= 2
            print(gap)
            
            
            

num = [31,9,10,23,49,15,11,7]
s = shellSort(num)
s.sort()
print(s.lst)

class QuickSort:
    def __init__(self, num):
        self.lst = num
        
    def swap(self, a, b):
        tmp = self.lst[a]
        self.lst[a] = self.lst[b]
        self.lst[b] = tmp
    def MedianofThree(self,  left, right):
        mid = self.lst[(left+right)//2]
        lft = self.lst[left]
        rt = self.lst[right]
        if (mid <= rt <= lft) or (lft <= rt <= mid):
            return right
        elif  (rt < mid < lft) or (lft <= mid <= rt):
            return (left+right)//2
        else:
            return left
    def sort(self, left, right):
        print(self.lst)
        # 재귀적인 반복
        if left == right:
            return
        pivot = self.MedianofThree(left, right)
        lft = left
        rt = right
        # partitining
        while True:
            if lft >= rt:
                self.swap(pivot, rt)
                break
            if self.lst[lft] > pivot:
                pass
            else:
                lft += 1
            if self.lst[rt] < pivot:
                pass
            else:
                rt +- 1  
            if  self.lst[lft] > pivot and self.lst[rt] < pivot:
                self.swap(lft, rt)
        self.sort(self, left, pivot)
        self.sort(self, pivot, right)

            
print("HI")

num = [31,9,10,23,49,15,11,7]
s = QuickSort(num)
print(s.lst)
s.sort(0, len(num)-1)
print(s.lst)
print(s.lst)