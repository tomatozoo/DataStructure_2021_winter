class frame:
    def __init__(self, index):
        self.index = index
        self.first = 0
        self.second = 0
        self.next = None
        self.result = None
        self.f_total = 0
        
    def getNumber(self):
        if self.index < 10:
            self.first, self.second = input(f"{self.index+1} 프레임 : ").split(' ')
        else:
            self.first, self.second = input("보너스 드로우 : ").split(' ')
        
        self.f_total = int(self.first) + int(self.second)
        
    def current(self):
        if self.index < 10:
            if int(self.first) == 10:
                self.result = 'X'
            elif int(self.first) + int(self.second) == 10:
                self.result = '/'
            else:
                self.result = '-'
                
            
class bowling:
    def __init__(self):
        self.head = None
        self.count = None
    def calculate(self):
        pass
    def pastCal(self):
        pass

def bowling():
    
    total = 0
    result = 'X'

    for i in range(11):
        pass

    
    
bowling()