class Node:
    pass
class Huffman:
    def __init__(self, char, num):
        self.char = [char for _, char in sorted(zip(num, char))]
        self.num = [num for num, _ in sorted(zip(num, char))]
        print(self.char)
        print(self.num)
    def tree(self):
        pass
    def codes(self):
        pass        

# character
char = ['w', 'f', 'r', 'm', 'e', 'd', 'o', 't', 'i', 'a', 'n',' ']
# frequency
num = [3,3,2,2,6,4,4,3,1,1,2,1]

print(len(char), len(num))

# step 0. sort char and num
char = [char for _, char in sorted(zip(num, char))]
num = [num for num, _ in sorted(zip(num, char))]
print(char)
print(num)

