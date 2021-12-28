class Maze:
    def __init__(self):
        self.maze = [[1,1,1,1,1,1,1,1,1,1],\
                     [1,0,0,1,0,0,0,0,1,1], \
                     [1,1,0,1,0,1,1,0,0,1],\
                     [1,0,0,0,0,1,1,1,1,1],\
                     [1,0,1,1,0,1,0,0,0,1],\
                     [1,0,0,1,0,1,1,0,1,1],\
                     [1,1,0,0,1,0,0,0,1,1],\
                     [1,1,1,0,0,0,1,0,0,1], \
                     [1,0,0,0,1,0,1,1,1,1],\
                     [1,1,1,1,1,1,1,1,1,1]]
        self.mark = [[0]*10 for i in range(10)]
        self.stack = [[1,1]]
        self.found = False
    def empty(self):
        return len(self.stack) == 0
    def push(self, row, col):
        self.stack.insert(0, [row, col])
    def view(self):
        for i in self.maze:
            print(i)
    def explore(self):
        while True:
            if len(self.stack) == 0:
                print("FAILED")
                return 
            elif self.stack[-1] == [9,9]:
                print("Solution : ", self.stack)
                return
            else:
                self.found = False
                tmp = self.stack[0]
                if self.maze[tmp[0]-1][tmp[1]]==0:
                    self.found = True
                    self.nextCandid = [tmp[0]-1, tmp[1]]
                elif self.maze[tmp[0]+1][tmp[1]]==0:
                    self.found = True     
                    self.nextCandid = [tmp[0]+1, tmp[1]]           
                elif self.maze[tmp[0]][tmp[1]-1]==0:
                    self.found = True          
                    self.nextCandid = [tmp[0], tmp[1]-1]       
                elif self.maze[tmp[0]][tmp[1]+1]==0:
                    self.found = True 
                    self.nextCandid = [tmp[0], tmp[1]+1]
                if self.found == True:
                    self.stack.insert(0, self.nextCandid)
                    print(self.stack)
                else:
                    self.stack.pop()



m = Maze()
m.explore()