import sys


class BST:
    def __init__(self):
        self.size = 1 << 22
        self.tree = [None] * self.size
    
    def add(self, v):
        ind = 1
        while ind < self.size:
            if self.tree[ind] is None:
                self.tree[ind] = v
                return "DONE"
            elif self.tree[ind] == v:
                return "ALREADY"
            elif v  < self.tree[ind]:
                ind = ind << 1
            else:
                ind = ind << 1 | 1
        return "ERROR"
    
    def search(self, v):
        ind = 1
        while ind < self.size:
            if self.tree[ind] is None:
                return "NO"
            elif self.tree[ind] == v:
                return "YES"
            elif v  < self.tree[ind]:
                ind = ind << 1
            else:
                ind = ind << 1 | 1
        return "NO"
    
    def printtree(self, ind=1, depth=0):
        if ind >= self.size or self.tree[ind] is None:
            return
        self.printtree(ind << 1, depth=depth+1)
        print('.'*depth + str(self.tree[ind]))
        self.printtree(ind << 1 | 1, depth=depth+1)


bst = BST()

for line in sys.stdin:
    line = line.strip()
    if line.startswith("ADD"):
        s, value = line.split()
        print(bst.add(int(value)))
    elif line.startswith("SEARCH"):
        s, value = line.split()
        print(bst.search(int(value)))
    elif line == "PRINTTREE":
        bst.printtree()