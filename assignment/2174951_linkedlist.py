class Node:
    def __init__(self):
        self.data = 0
        self.link = None
        self.f_total = 0
        self.frame = []

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.rear = None
        self.count = 0
    def isEmpty(self):
        return not self.head # head가 None
    def find(self, index):
        cnt = 0
        tmp = self.head
        while (cnt != index):
            tmp = tmp.link
            cnt += 1
        return tmp
    def appendNode(self, node):
        if self.head == None:
          self.head = node
          self.rear = node
        else:
          self.rear.link = node
          self.rear = node 
        self.count += 1
    def print(self):
        tmp = self.head
        while tmp != None:
          print(tmp.frame, end=' ')
          tmp = tmp.link



def bowling():
  total = 0
  result = 'X'

  s = SinglyLinkedList()

  for i in range(11):
    tmp = Node()
    # input
    if i < 10:
      first, second = input(f"{i+1} 프레임 : ").split(' ')
    else:
        first, second = input("보너스 드로우 : ").split(' ')
    f_total = int(first) + int(second)
    # current result 
    if i < 10:
      if int(first) == 10:
        # strike
        result = 'X'
        tmp.frame = [int(first), int(second), result, ' ']
      elif int(first) + int(second) == 10:
        # spare
        result = '/'
        tmp.frame = [int(first), int(second), result, ' ']

      else:
        # none
        result = '-'
        total += f_total
        tmp.frame = [int(first), int(second), result, f_total]
      

    else:
      tmp.frame = [int(first), int(second)]
      
    s.appendNode(tmp)
    # past strike / spare
    # 전전 strike 점수 계산해주기
    
    if s.count >= 3:
      pastpastFrame = s.find(s.count-3)
      pastFrame = s.find(s.count-2)
      if pastpastFrame.frame[3] == ' ':
        if pastpastFrame.frame[2] == 'X':
          pastpastFrame.frame[3] = int(first) + pastpastFrame.frame[0] + pastFrame.frame[0]
          total += pastpastFrame.frame[3]
    if s.count >= 2:
      pastFrame = s.find(s.count-2)
      if pastFrame.frame[3] == ' ':
        if pastFrame.frame[2] == '/':
          pastFrame.frame[3] = pastFrame.frame[0] + pastFrame.frame[1] + int(first)
          total += pastFrame.frame[3]
        elif pastFrame.frame[2] == 'X':
          if int(first) == 10:
            if i == 10:
              pastFrame.frame[3] = pastFrame.frame[0] + int(first) + int(second)
              total += pastFrame.frame[3]
          else:
            pastFrame.frame[3] = pastFrame.frame[0] + int(first) + int(second)
            total += pastFrame.frame[3]

    if i == 9:
      pass
    else:
      s.print()
      print()
      print("Total = ", total)
      print()


bowling()