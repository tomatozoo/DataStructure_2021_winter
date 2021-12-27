class frame:
    def __init__(self, index, first, second, result):
        self.index = index
        self.first = first
        self.second = second
        self.result = result
        self.next = None
        
class bowling:
    def __init__(self):
        self.head = None
        self.count = None

def bowl():
    
    total = 0
    b = bowling()
    
    for i in range(11):
        if i < 10:
            first, second = input(f"{i+1} 프레임 : ").split(' ')
        else:
            first, second = input("보너스 드로우 : ").split(' ')
        f_total = int(first) + int(second)

        if i < 10:
            if int(first) == 10:
                # strike
                result = 'X'
                tmp = frame(i, int(first), int(second), result, ' ')
            elif int(first) + int(second) == 10:
                pass
                

    
    
    
bowl()