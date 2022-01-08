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