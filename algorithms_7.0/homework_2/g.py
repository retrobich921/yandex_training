import sys
from math import log2, ceil

sys.setrecursionlimit(2000000)


class SegmentTree:
    def __init__(self, n, a):
        self.n = n
        self._base = 1 << ceil(log2(n)) if n > 0 else 1
        # Каждый узел хранит (max_zeros, prefix_zeros, suffix_zeros, total_length_of_segment)
        self.tree = [(0, 0, 0, 0)] * (2 * self._base) 

        for i in range(n):
            if a[i] == 0:
                self.tree[self._base + i] = (1, 1, 1, 1)
            else:
                self.tree[self._base + i] = (0, 0, 0, 1)
        
        for i in range(self._base - 1, 0, -1):
            self.tree[i] = self._merge(self.tree[i << 1], self.tree[i << 1 | 1])

    def _merge(self, left_val, right_val):
        left_max, left_pref, left_suff, left_len = left_val
        right_max, right_pref, right_suff, right_len = right_val

        new_max = max(left_max, right_max, left_suff + right_pref)

        new_pref = left_pref
        if left_pref == left_len:
            new_pref += right_pref

        new_suff = right_suff
        if right_suff == right_len:
            new_suff += left_suff
        
        new_total_len = left_len + right_len

        return (new_max, new_pref, new_suff, new_total_len)

    def UPDATE(self, index, value):
        idx = self._base + (index - 1)
        if value == 0:
            self.tree[idx] = (1, 1, 1, 1)
        else:
            self.tree[idx] = (0, 0, 0, 1)
        
        idx >>= 1 
        while idx >= 1:
            self.tree[idx] = self._merge(self.tree[idx << 1], self.tree[idx << 1 | 1])
            idx >>= 1

    def QUERY(self, query_l, query_r):
        query_l_0_indexed = query_l - 1
        query_r_0_indexed = query_r - 1
        
        result = self._query_recursive(1, 0, self._base, query_l_0_indexed, query_r_0_indexed)
        return result[0]

    def _query_recursive(self, node, current_node_l, current_node_r_exclusive, query_l_inclusive, query_r_inclusive):
        if current_node_r_exclusive <= query_l_inclusive or current_node_l > query_r_inclusive:
            return (0, 0, 0, 0)

        if query_l_inclusive <= current_node_l and current_node_r_exclusive - 1 <= query_r_inclusive:
            return self.tree[node]

        mid = (current_node_l + current_node_r_exclusive) // 2
        
        left_res = self._query_recursive(node << 1, current_node_l, mid, query_l_inclusive, query_r_inclusive)
        right_res = self._query_recursive(node << 1 | 1, mid, current_node_r_exclusive, query_l_inclusive, query_r_inclusive)

        return self._merge(left_res, right_res)


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    tree = SegmentTree(n, a)
    
    m = int(input())
    
    results = []
    for _ in range(m):
        line = input().split()
        query_type = line[0]
        
        if query_type == 'UPDATE':
            index, value = int(line[1]), int(line[2])
            tree.UPDATE(index, value)
        elif query_type == 'QUERY':
            l, r = int(line[1]), int(line[2])
            results.append(str(tree.QUERY(l, r)))
            
    print('\n'.join(results))


if __name__ == "__main__":
    solve()
