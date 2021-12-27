class Maze:

    def __init__(self):
        self.maze=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ], \
        [1, 0, 0, 1, 0, 0, 0, 0, 1, 1 ], \
        [1, 1, 0, 1, 0, 1, 1, 0, 0, 1 ], \
        [1, 0, 0, 0, 0, 1, 1, 1, 1, 1 ], \
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 1 ], \
        [1, 0, 0, 1, 0, 1, 1, 0, 1, 1 ], \
        [1, 1, 0, 0, 1, 0, 0, 0, 1, 1 ], \
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1 ], \
        [1, 0, 0, 0, 1, 0, 1, 1, 'X', 1 ], \
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]]
        self.mark=[]
        self.stack = []
        self.found = False

    def empty(self):
        return len(self.stack)==0
    def push(self, row, col):
        self.stack.append((row, col))
    def view(self):
        print("stack", self.stack)

    def explore(self):
        self.mark[1][1] = 1 # 방문해서 1로 바꾼다
        self.push(1,1)
        while not self.empty() and not self.found:
            if not move_next:
                # 다시 이전 위치로 돌아가서 탐색한다. 
                row, col = self.stack.pop()
            move_next = False
            for x, y in [(0,-1),(1,0),(0,1), (-1,0)]: # 북, 동, 남, 서
                next_col = col + x
                next_row = row + y
                if self.maze[next_row][next_col] == 'X':
                    self.push(row, col)
                    self.push(next_row, next_col)
                    self.found = True
                    # 탈출 성고
                    break
                elif self.maze[next_row][next_col]==0 and self.mark[next_row][next_col]==0:
                    # 아직 도착 못함
                    # 아직 기회 남음.
                    self.mark[next_row][next_col]=1
                    print(next_row, next_col, "is visited")
                    self.push(row, col)
                    row = next_row
                    col = next_col
                    move_next = True
                    break
        if not self.found: 
            print("No path found")
        else: 
            print("Path found:")
            self.view() # 거쳐간 경로 출력함