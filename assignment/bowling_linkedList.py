class Node:
    def __init__(self, item):
        self.data = item
        self.link = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.rear = None
    def addNode(self):
        pass
    def isEmpty(self):
        return not self.head # head가 None
    def addRear(self):
        pass

def bowling():
    total = 0
    frame = []
    stack = []
    result = 'X'
    
    for i in range(11):
        if i < 10:
            first, second = input(f"{i+1} 프레임 : ").split(' ')
        else:
            first, second = input("보너스 드로우 : ").split(' ')
            
        f_total = int(first) + int(second)
        
        # current result - create node

        if i < 10:
                
            if int(first) == 10:
                # strike
                result = 'X'
                frame.append([int(first), int(second), result, ' '])

            elif int(first) + int(second) == 10:
                # spare
                result = '/'
                frame.append([int(first), int(second), result, ' '])

            else:
                # none
                result = '-'
                total += f_total
                frame.append([int(first), int(second), result, f_total])
        else:
            frame.append([int(first), int(second)])
        
        # past strike / spare
        # past strike / spare    
        if len(frame) >= 3 and frame[-3][3] == ' ':
            if frame[-3][2] == '/': # 불가능
                pass
            elif frame[-3][2] == 'X': # 더해주기
                frame[-3][3] = (frame[-3][0] + frame[-2][0] + int(first))
                total += frame[-3][3]    
        
        if len(frame) >= 2 and frame[-2][3] == ' ':
            if frame[-2][2] == '/':
                frame[-2][3] = (frame[-2][0] + frame[-2][1] + int(first))
                total += frame[-2][3]
            elif frame[-2][2] == 'X':
                if int(first) == 10: # current도 strike
                    if i == 10:
                        frame[-2][3] = frame[-2][0] + int(first) + int(second)
                        total += frame[-2][3]
                else:
                    # current는 strike 아님
                    frame[-2][3] = (frame[-2][0] + int(first) + int(second))
                    total += frame[-2][3]
                
     

        if i == 9:
            pass
        else:
            print(frame)
            print("Total = ", total)
            print()

        stack.append((int(first), int(second), result, f_total))
    

    
    
bowling()