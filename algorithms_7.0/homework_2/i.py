import sys
from math import log2, ceil

sys.setrecursionlimit(2000000)


class SegmentTree:
    def __init__(self, n, a):
        self.n = n
        self._base = 1
        while self._base < n:
            self._base *= 2
        
        self.tree = [(0, 0)] * (2 * self._base)

        for i in range(n):
            self.tree[self._base + i] = (a[i], 0)
        
        for i in range(self._base - 1, 0, -1):
            self.tree[i] = (max(self.tree[i << 1][0], self.tree[i << 1 | 1][0]), 0)


    def _push_down(self, node):
        if self.tree[node][1] != 0 and node < self._base:
            lazy_val = self.tree[node][1]

            self.tree[node * 2] = (self.tree[node * 2][0] + lazy_val, self.tree[node * 2][1] + lazy_val)
            self.tree[node * 2 + 1] = (self.tree[node * 2 + 1][0] + lazy_val, self.tree[node * 2 + 1][1] + lazy_val)
            
            self.tree[node] = (self.tree[node][0], 0)


    def update_range(self, query_l, query_r, add_value):
        self._update_recursive(1, 0, self._base - 1, query_l - 1, query_r - 1, add_value)


    def _update_recursive(self, node, current_l, current_r, query_l_inclusive, query_r_inclusive, add_value):
        if current_l > query_r_inclusive or current_r < query_l_inclusive:
            return

        if query_l_inclusive <= current_l and current_r <= query_r_inclusive:
            self.tree[node] = (self.tree[node][0] + add_value, self.tree[node][1] + add_value)
            return

        self._push_down(node)

        mid = (current_l + current_r) // 2
        self._update_recursive(node * 2, current_l, mid, query_l_inclusive, query_r_inclusive, add_value)
        self._update_recursive(node * 2 + 1, mid + 1, current_r, query_l_inclusive, query_r_inclusive, add_value)
        
        self.tree[node] = (max(self.tree[node * 2][0], self.tree[node * 2 + 1][0]), self.tree[node][1])


    def query_max(self, query_l, query_r):
        return self._query_recursive(1, 0, self._base - 1, query_l - 1, query_r - 1)


    def _query_recursive(self, node, current_l, current_r, query_l_inclusive, query_r_inclusive):
        if current_l > query_r_inclusive or current_r < query_l_inclusive:
            return -sys.maxsize

        if query_l_inclusive <= current_l and current_r <= query_r_inclusive:
            return self.tree[node][0]

        self._push_down(node)

        mid = (current_l + current_r) // 2
        left_max = self._query_recursive(node * 2, current_l, mid, query_l_inclusive, query_r_inclusive)
        right_max = self._query_recursive(node * 2 + 1, mid + 1, current_r, query_l_inclusive, query_r_inclusive)
        
        return max(left_max, right_max)


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    tree = SegmentTree(n, a)
    
    m = int(input())
    
    results = []
    for _ in range(m):
        line = input().split()
        query_type = line[0]
        
        if query_type == 'a':
            l, r, add_value = int(line[1]), int(line[2]), int(line[3])
            tree.update_range(l, r, add_value)
        elif query_type == 'm':
            l, r = int(line[1]), int(line[2])
            results.append(str(tree.query_max(l, r)))
            
    print(' '.join(results))


if __name__ == "__main__":
    solve()
