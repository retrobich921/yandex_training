import sys
from math import log2, ceil

sys.setrecursionlimit(2000000)


class SegmentTree:
    def __init__(self, n, a):
        self.n = n
        self._base = 1
        while self._base < n:
            self._base *= 2
        
        self.tree = [0] * (2 * self._base)

        for i in range(n):
            self.tree[self._base + i] = a[i]


    def _push_down(self, node):
        if node < self._base:
            self.tree[node * 2] += self.tree[node]
            self.tree[node * 2 + 1] += self.tree[node]
            self.tree[node] = 0


    def update_range(self, query_l, query_r, add_value):
        self._update_recursive(1, 0, self._base - 1, query_l - 1, query_r - 1, add_value)


    def _update_recursive(self, node, current_l, current_r, query_l, query_r, add_value):
        if current_l > query_r or current_r < query_l:
            return

        if query_l <= current_l and current_r <= query_r:
            self.tree[node] += add_value
            return

        self._push_down(node)

        mid = (current_l + current_r) // 2
        self._update_recursive(node * 2, current_l, mid, query_l, query_r, add_value)
        self._update_recursive(node * 2 + 1, mid + 1, current_r, query_l, query_r, add_value)


    def get_value(self, index):
        return self._get_value_recursive(1, 0, self._base - 1, index - 1)


    def _get_value_recursive(self, node, current_l, current_r, target_index):
        if current_l == current_r:
            return self.tree[node]

        self._push_down(node)

        mid = (current_l + current_r) // 2
        if target_index <= mid:
            return self._get_value_recursive(node * 2, current_l, mid, target_index)
        else:
            return self._get_value_recursive(node * 2 + 1, mid + 1, current_r, target_index)


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
        elif query_type == 'g':
            index = int(line[1])
            results.append(str(tree.get_value(index)))
            
    print('\n'.join(results))


if __name__ == "__main__":
    solve()
