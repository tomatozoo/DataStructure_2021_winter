class NQeens:
    
    def __init__(self, size): # 순열 문제와 같다. 
        self.size = size
        self.solutions = 0
        self.col = [-1] * size
        
    def put_queen(self, row):
        if row==self.size:
            self.show_board()
            self.solutions += 1
        else:
            for col in range(self.size):
                if self.check_pos(row, col):
                    self.col[row] = col
                    # queen을 놓음
                    self.put_queen(row+1)
                    
    def check_pos(self, rows, col):
        # 잡아먹는 queen이 있는지 check
        for i in range(rows):
            if self.col[i] == col or \
                self.col[i] - i == col - rows or \
                self.col[i] + i ==col + rows:
                    return False
        return True
            
    def show_board(self):
        for row in range(self.size):
            line = ""
            
            for column in range(self.size):
                if self.col[row] == column:
                    line += 'Q'
                else:
                    line += "+ "
            print(line)
        print()

N = 4
q = NQeens(N)
q.put_queen(0)
print(q.solutions, "solutions found")