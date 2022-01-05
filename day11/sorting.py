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
    pass