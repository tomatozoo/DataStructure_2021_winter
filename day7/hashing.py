class hashing:
    def __init__(self, size):
        self.size = size
        self.table = [None]*size
    
    def hf(self, key):
        # 버킷 주소로 쓴다. 
        # 해싱의 원리임
        total= 0
        for s in key:
            total += ord(s)
        return total % self.size
