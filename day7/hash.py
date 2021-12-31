class Hashing:
    def __init__(self, size, hf):
        self.size = size
        self.table = [None]*size
        self.collision = []
    def hf(self, key):
        total = 0
        for s in key:
            total += ord(s)
        return total % self.size
    def add_table(self, sym):
        bucket = self.hf(sym)
        if self.table[bucket] is None:
            self.table[bucket] = sym
        else:
            self.collision.append(sym)
    def show_table(self):
        i = 0
        for item in self.table:
            print(i, item)
            i += 1
symbol = ['for', 'while', 'if', 'else', 'elif',\
    'def', 'class', 'self', 'return', 'range', 'list',\
        'tuple', 'ceil']
h = Hashing(26, 1)
print("Symbols = ", len(symbol))
for item in symbol:
    h.add_table(item)
h.show_table()
print("Hash function = ", h.hf)
print("Collision = ", h.collision)
print("collisions = ", len(h.collision))