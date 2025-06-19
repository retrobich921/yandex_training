import sys
from math import log2, ceil

sys.setrecursionlimit(2000000)


class SegmentTree:
    def __init__(self, n, a):
        self.n = n
        self._base = 1 << ceil(log2(n)) if n > 0 else 1
        self.tree = [0] * (2 * self._base)

        for i in range(n):
            self.tree[self._base + i] = 1 if a[i] == 0 else 0
        
        for i in range(self._base - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, index, value):
        idx = self._base + (index - 1)
        self.tree[idx] = 1 if value == 0 else 0
        
        idx >>= 1
        while idx >= 1:
            self.tree[idx] = self.tree[idx << 1] + self.tree[idx << 1 | 1]
            idx >>= 1

    def query_kth_zero(self, k, query_l, query_r):
        query_l_0_indexed = query_l - 1
        query_r_0_indexed = query_r - 1
        
        return self._query_kth_zero_recursive(1, 0, self._base, query_l_0_indexed, query_r_0_indexed, k)

    def _query_kth_zero_recursive(self, node, current_node_l, current_node_r_exclusive, query_l_inclusive, query_r_inclusive, k):
        if current_node_r_exclusive <= query_l_inclusive or current_node_l > query_r_inclusive:
            return -1
        
        if self.tree[node] == 0:
            return -1

        if current_node_r_exclusive - current_node_l == 1:
            if self.tree[node] == 1 and query_l_inclusive <= current_node_l <= query_r_inclusive and k == 1:
                return current_node_l + 1
            else:
                return -1

        mid = (current_node_l + current_node_r_exclusive) // 2
        
        left_zeros_count = self._get_zeros_in_overlap(node << 1, current_node_l, mid, query_l_inclusive, query_r_inclusive)

        if k <= left_zeros_count:
            return self._query_kth_zero_recursive(node << 1, current_node_l, mid, query_l_inclusive, query_r_inclusive, k)
        else:
            return self._query_kth_zero_recursive(node << 1 | 1, mid, current_node_r_exclusive, query_l_inclusive, query_r_inclusive, k - left_zeros_count)

    def _get_zeros_in_overlap(self, node, current_node_l, current_node_r_exclusive, query_l_inclusive, query_r_inclusive):
        if current_node_r_exclusive <= query_l_inclusive or current_node_l > query_r_inclusive:
            return 0

        if query_l_inclusive <= current_node_l and current_node_r_exclusive <= query_r_inclusive + 1:
            return self.tree[node]
        
        mid = (current_node_l + current_node_r_exclusive) // 2
        return self._get_zeros_in_overlap(node << 1, current_node_l, mid, query_l_inclusive, query_r_inclusive) + \
               self._get_zeros_in_overlap(node << 1 | 1, mid, current_node_r_exclusive, query_l_inclusive, query_r_inclusive)


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    tree = SegmentTree(n, a)
    
    m = int(input())
    
    results = []
    for _ in range(m):
        query_parts = input().split()
        
        if query_parts[0] == 's':
            l, r, k = int(query_parts[1]), int(query_parts[2]), int(query_parts[3])
            results.append(str(tree.query_kth_zero(k, l, r)))
        elif query_parts[0] == 'u':
            index, value = int(query_parts[1]), int(query_parts[2])
            tree.update(index, value)
            
    print(' '.join(results))


if __name__ == "__main__":
    solve()