class SelectionSort:
    def __init__(self, num):
        self.num = num
        self.size = len(num)
        print("Selection Sort", self.num)
    def __str__(self):
        for i in range(self.size):
            print("%2d " % self.num[i])
    def sort(self):
        n = self.size
        for i in range(n-1):
            min = i
            for j in range(i+1, n):
                if self.num[j] < self.num[min]: min = j
            self.num[i], self.num[min] = self.num[min], self.num[i]
            print(self.num)

num = [31, 9, 10, 23, 49, 15, 11, 7]
s = SelectionSort(num)
s.sort()

class Bubblesort:
    def __init__(self, num):
        self.num = num
        self.size = len(num)
        print("bubble sort", self.num)
    def __str__(self):
        for i in range(self.size):
            print("%2d " % self.num[i])
    def swap(self, a, b):
        self.num[a], self.num[b] = self.num[b], self.num[a]
    def sort(self):
        n = self.size
        for i in range(n-1):
            flag = 0
            for j in range(0, n-i-1):
                if self.num[j] > self.num[j+1]:
                    self.swap(j, j+1)
                    flag = 1
            if flag == 0: break
            print(self.num)

num = [13,25,9,12,34,52,49,17,5,8]
s = Bubblesort(num)
s.sort()