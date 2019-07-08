class UnionFind:
    def __init__(self, size):
        self.p = [i for i in range(size)]

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)


uf = UnionFind(10)

uf.union(0, 1)
uf.union(1, 2)
uf.union(0, 2)

print(uf.find(0) == uf.find(2))
