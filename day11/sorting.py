class InsertionSort:
    def __init__(self, num):
        self.num = num
        self.size = len(num)
        print("Insertion Sort", self.num)
    def __str__(self):
        for i in range(self.size):
            print("%2d " % self.num[i])
    def sort(self):
        for i in range(1, self.size):
            pivot = self.num[i]
            j = i-1
            while j >= 0 and pivot < self.num[j]: # j를 밀어내야한다
                self.num[j+1] = self.num[j]
                j-= 1
            self.num[j+1] = pivot
            print(self.num)

num = [13, 25, 9, 12, 34]
c = InsertionSort(num)
c.sort()

class ShellSort:
    def __init__(self, num):
        self.num = num
        self.size = len(num)
        print("Shells Sort", self.num)
    def __str__(self):
        for i in range(self.size):
            print("%2d " % self.num[i])
    def sort(self):
        n = self.size
        gap = n//2
        while gap > 0: # 갭을 정해준다
            if gap % 2 == 0: gap += 1 # 갭을 홀수로 정한다
            for i in range(gap, n): # gap에서 self.size까지
                h = 1 
                while i * h < n:
                    j = i*h # gap만큼 증가한 index를 위한 변수
                    temp = self.num[i*h]
                    while j >= gap: # insertion sort
                        if temp < self.num[j-gap]: # 정렬 필요
                            self.num[j] = self.num[j-gap]
                        else: break # 이미 정렬된 것
                        j -= gap
                    self.num[j] = temp
                    h += 1
            print(gap, self.num)
            gap //= 2    

num = [13, 25, 9, 12, 34]
c = ShellSort(num)
c.sort()

def QuickSort(A, start, end):
    if start >= end: 
        print(A[start])
        return
    m = Partition(A, start, end)
    QuickSort(A, start, m-1)
    QuickSort(A, m+1, end)

def Partition(A, start, end):
    pivot = start
    i = start
    j = end + 1
    while True:
        while True:
            i+=1
            if i<=end or A[j] < A[pivot]: break
        while True:
            j -= 1
            if A[j] > A[pivot] or j>=start: break
        if i < j:
            A[i], A[j] = A[j], A[i]
        else: break
    A[start], A[j] = A[j], A[start]
    return j

class QuickSort:
    def __init__(self, num):
        self.num = num
        self.size = len(num)
        print("Quick Sort", self.num)
    def swap(self, a, b):
        self.num[a], self.num[b] = self.num[b], self.num[a]
    def sort(self, left, right):
        if left < right:
            i = left
            j = right + 1
            pivot = num[left]
            while True:
                while True:
                    i+= 1
                    if i > right or num[i] >= pivot:
                        break
                while True:
                    j -= 1
                    if j < left or num[j] <= pivot:
                        break
                if i < j:
                    num[i], num[j] = num[j], num[i]
                else:
                    break
            num[left], num[j] = num[j], num[left]
            if left != j:
                print(self.num)
            self.sort(left, j-1)
            self.sort(j+1, right)

num = [26,5,37,1,61,11,59,15,48,19]
s = QuickSort(num)
s.sort(0, len(num)-1)

class MergeSort:
    def __init__(self, num):
        self.num = num
    def mergesort(self, left, right):
        if right > left:
            mid = (left + right) // 2 # 분할
            self.mergesort(left, mid) # sort
            self.mergesort(mid+1, right) # sort
            self.merge(left, mid+1, right) # merge
    def merge(self, left, mid, right): # 1st = [left..mid-1] 2nd = [mid..right]
        pos = left
        left_end = mid - 1
        n = right - left + 1
        temp = [None] * self.size
        while left <= left_end and mid <= right:
            # 앞 부분을 비교해서 작은 요소를 먼저 넣는다
            if self.num[left] <= self.num[mid]: 
                temp[pos] = num[left]
                pos = pos + 1
                left = left + 1
            else:
                temp[pos] = num[mid]
                pos += 1
                mid += 1
        while left <= left_end:
            temp[pos] = num[left]
            left += 1
            pos += 1
        while mid <= right:
            temp[pos] = num[mid]
            mid += 1
            pos += 1
        for i in range(n):
            # temp를 num 배열에 복사해준다
            self.num[right] = temp[right]
            right -= 1
            
num = [40,15,34,29,3,10,9,17,37]
s = MergeSort(num)
s.mergesort(0, len(num)-1)