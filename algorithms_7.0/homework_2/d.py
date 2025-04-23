from math import log2, ceil


class SegmentTree():
    def __init__(self, n, a):
        size = 1 << (ceil(log2(n)) + 1)
        self.tree = [[0, 0]] * size
        
        self.n = n
        for i in range(n):
            self.tree[(size >> 1) + i] = [a[i], i+1]
            # print((size // 2 + i)>>1)

    def filling_max(self):
        for i in range((len(self.tree) >> 1) - 1, 0, -1):
            if self.tree[i << 1 | 1][0] > self.tree[i << 1][0]:
                self.tree[i] = self.tree[i << 1 | 1]
            elif self.tree[i << 1 | 1][0] < self.tree[i << 1][0]:
                self.tree[i] = self.tree[i << 1]
            else:
                self.tree[i] = [self.tree[i << 1][0], self.tree[i << 1][1] + self.tree[i << 1 | 1][1]]
        # print(*self.tree)

    def filling_ind_max(self):
        for i in range((len(self.tree) >> 1) - 1, 0, -1):
            if self.tree[i << 1 | 1][0] > self.tree[i << 1][0]:
                self.tree[i] = self.tree[i << 1 | 1]
            elif self.tree[i << 1 | 1][0] < self.tree[i << 1][0]:
                self.tree[i] = self.tree[i << 1]
            else:
                self.tree[i] = [self.tree[i << 1][0], self.tree[i << 1][1]]

    def query_max_count(self, node, left, right, l, r):
        if r <= left or right <= l:
            return [-float("inf"), 0]

        if l <= left and right <= r:
            return self.tree[node]

        mid = (left + right) >> 1
        left_result = self.query_max_count(node << 1, left, mid, l, r)
        right_result = self.query_max_count(node << 1 | 1, mid, right, l, r)

        if left_result[0] > right_result[0]:
            return left_result
        elif right_result[0] > left_result[0]:
            return right_result
        else:
            return [left_result[0], left_result[1] + right_result[1]]
        
    def query_ind_max(self, node, left, right, l, r):
        if r <= left or right <= l:
            return [-float("inf"), 0]

        if l <= left and right <= r:
            return self.tree[node]

        mid = (left + right) >> 1
        left_result = self.query_ind_max(node << 1, left, mid, l, r)
        right_result = self.query_ind_max(node << 1 | 1, mid, right, l, r)

        if left_result[0] > right_result[0]:
            return left_result
        elif right_result[0] > left_result[0]:
            return right_result
        else:
            return [left_result[0], left_result[1]]

    def upgrade_max(self, ind, value):
        self.tree[ind] = [value, ind - (len(self.tree) >> 1)]
        self.upgrade_max_ind(ind=ind)

    def upgrade_max_ind(self, ind):
        if 0 < (ind >> 1) < len(self.tree):
            if self.tree[ind >> 1][0] < self.tree[ind][0]:
                self.tree[ind >> 1] = self.tree[ind]
                self.upgrade_max_ind(ind >> 1)


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    tree = SegmentTree(n, a)
    tree.filling_ind_max()
    q = int(input())
    ans = []
    for i in range(q):
        query, l_i, r_v = input().split()
        l_i, r_v = int(l_i), int(r_v)
        if query == 's':
            ans += [tree.query_ind_max(1, 0, len(tree.tree) >> 1, l_i-1, r_v)[0]]
        else:
            tree.upgrade_max((len(tree.tree) >> 1) + l_i - 1, r_v)
        # print(*tree.tree)
    
    print(*ans)

if __name__ == "__main__":
    solve()