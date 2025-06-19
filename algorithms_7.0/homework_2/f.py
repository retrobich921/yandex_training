import sys
from math import log2, ceil

sys.setrecursionlimit(2000000)


class SegmentTree:
    def __init__(self, n, a):
        self.n = n
        self._base = 1 << ceil(log2(n)) if n > 0 else 1
        self.tree = [0] * (2 * self._base) 

        for i in range(n):
            self.tree[self._base + i] = a[i]
        
        for i in range(self._base - 1, 0, -1):
            self.tree[i] = max(self.tree[i << 1], self.tree[i << 1 | 1])

    def update(self, index, value):
        idx = self._base + (index - 1)
        self.tree[idx] = value
        
        idx >>= 1
        while idx >= 1:
            self.tree[idx] = max(self.tree[idx << 1], self.tree[idx << 1 | 1])
            idx >>= 1

    def query_first_greater_equal(self, query_start_index_inclusive, value_x):
        query_start_0_indexed = query_start_index_inclusive - 1
        
        return self._query_first_greater_equal_recursive(1, 0, self._base, query_start_0_indexed, value_x)

    def _query_first_greater_equal_recursive(self, node, current_node_l, current_node_r_exclusive, query_start_index_inclusive, value_x):
        if self.tree[node] < value_x:
            return -1
        
        if current_node_r_exclusive <= query_start_index_inclusive:
            return -1

        if current_node_r_exclusive - current_node_l == 1: 
            if self.tree[node] >= value_x and current_node_l >= query_start_index_inclusive:
                return current_node_l + 1 
            else:
                return -1

        mid = (current_node_l + current_node_r_exclusive) // 2
        
        if self.tree[node << 1] >= value_x: 
            left_result = self._query_first_greater_equal_recursive(node << 1, current_node_l, mid, query_start_index_inclusive, value_x)
            if left_result != -1:
                return left_result 

        if self.tree[node << 1 | 1] >= value_x: 
             right_result = self._query_first_greater_equal_recursive(node << 1 | 1, mid, current_node_r_exclusive, query_start_index_inclusive, value_x)
             if right_result != -1:
                 return right_result
        
        return -1 


def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    tree = SegmentTree(n, a)
    
    results = []
    for _ in range(m):
        query_parts = list(map(int, input().split()))
        
        query_type = query_parts[0]
        
        if query_type == 0: 
            index, value = query_parts[1], query_parts[2]
            tree.update(index, value)
        elif query_type == 1: 
            i, x = query_parts[1], query_parts[2]
            results.append(str(tree.query_first_greater_equal(i, x)))
            
    print('\n'.join(results))


if __name__ == "__main__":
    solve()