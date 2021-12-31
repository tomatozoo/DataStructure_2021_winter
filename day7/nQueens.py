class NQueens:
    def __init__(self, size):
        self.size = size
        self.solutions = 0
        self.col = [None] * size
    def put_queen(self, row):
        if row == self.size - 1:
            pass
        else:
            pass
    def check_pos(self, rows, col):
        pass
    def show_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.col[i] == j:
                    print('Q')
                else:
                    print('+')
            

N = 4
q = NQueens(N)
q.put_queen(0)
print(q.solutions, "Solutions found")