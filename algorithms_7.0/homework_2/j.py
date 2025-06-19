import sys
from math import log2, ceil

sys.setrecursionlimit(2000000)

P = 31
M = 10**9 + 7
INV_P_MINUS_1 = pow(P - 1, M - 2, M)

P_POWERS = []

def precompute_powers(n_max):
    global P_POWERS
    P_POWERS = [1] * (n_max + 1)
    for i in range(1, n_max + 1):
        P_POWERS[i] = (P_POWERS[i-1] * P) % M


class SegmentTree:
    def __init__(self, n, a):
        self.n = n
        self._base = 1
        while self._base < n:
            self._base *= 2
        
        self.tree = [(0, 0)] * (2 * self._base)
        self._build(1, 0, self._base - 1, a)


    def _build(self, node_idx, current_l, current_r, a):
        if current_l == current_r:
            if current_l < self.n:
                self.tree[node_idx] = (a[current_l], 0)
            else:
                self.tree[node_idx] = (0, 0)
            return

        mid = (current_l + current_r) // 2
        self._build(node_idx << 1, current_l, mid, a)
        self._build(node_idx << 1 | 1, mid + 1, current_r, a)
        
        left_hash = self.tree[node_idx << 1][0]
        right_hash = self.tree[node_idx << 1 | 1][0]
        right_len = (current_r - (mid + 1)) + 1
        self.tree[node_idx] = (self._combine_hashes(left_hash, right_hash, right_len), 0)


    def _combine_hashes(self, h1, h2, len2):
        return (h1 * P_POWERS[len2] + h2) % M


    def _hash_all_k(self, length, K):
        if length <= 0:
            return 0
        return (K * (P_POWERS[length] - 1 + M) % M * INV_P_MINUS_1) % M


    def _get_segment_length(self, current_l, current_r):
        return current_r - current_l + 1


    def _push_down(self, node_idx, current_l, current_r):
        lazy_val = self.tree[node_idx][1]
        
        if lazy_val != 0 and node_idx < self._base:
            mid = (current_l + current_r) // 2
            
            left_child_idx = node_idx << 1
            left_child_len = self._get_segment_length(current_l, mid)
            self.tree[left_child_idx] = (self._hash_all_k(left_child_len, lazy_val), lazy_val)

            right_child_idx = node_idx << 1 | 1
            right_child_len = self._get_segment_length(mid + 1, current_r)
            self.tree[right_child_idx] = (self._hash_all_k(right_child_len, lazy_val), lazy_val)
            
            self.tree[node_idx] = (self.tree[node_idx][0], 0)


    def assign_range(self, query_l, query_r, value_k):
        self._assign_recursive(1, 0, self._base - 1, query_l - 1, query_r - 1, value_k)


    def _assign_recursive(self, node_idx, current_l, current_r, query_l_inclusive, query_r_inclusive, value_k):
        if current_l > query_r_inclusive or current_r < query_l_inclusive:
            return

        if query_l_inclusive <= current_l and current_r <= query_r_inclusive:
            segment_len = self._get_segment_length(current_l, current_r)
            self.tree[node_idx] = (self._hash_all_k(segment_len, value_k), value_k)
            return

        self._push_down(node_idx, current_l, current_r)

        mid = (current_l + current_r) // 2
        self._assign_recursive(node_idx << 1, current_l, mid, query_l_inclusive, query_r_inclusive, value_k)
        self._assign_recursive(node_idx << 1 | 1, mid + 1, current_r, query_l_inclusive, query_r_inclusive, value_k)
        
        left_hash = self.tree[node_idx << 1][0]
        right_hash = self.tree[node_idx << 1 | 1][0]
        right_len = self._get_segment_length(mid + 1, current_r)
        self.tree[node_idx] = (self._combine_hashes(left_hash, right_hash, right_len), 0)


    def get_segment_hash(self, query_l, query_r):
        return self._get_hash_recursive(1, 0, self._base - 1, query_l - 1, query_r - 1)


    def _get_hash_recursive(self, node_idx, current_l, current_r, query_l_inclusive, query_r_inclusive):
        if current_l > query_r_inclusive or current_r < query_l_inclusive:
            return (0, 0)

        if query_l_inclusive <= current_l and current_r <= query_r_inclusive:
            return (self.tree[node_idx][0], self._get_segment_length(current_l, current_r))

        self._push_down(node_idx, current_l, current_r)

        mid = (current_l + current_r) // 2
        
        left_res_hash, left_res_len = self._get_hash_recursive(node_idx << 1, current_l, mid, query_l_inclusive, query_r_inclusive)
        right_res_hash, right_res_len = self._get_hash_recursive(node_idx << 1 | 1, mid + 1, current_r, query_l_inclusive, query_r_inclusive)

        combined_hash = self._combine_hashes(left_res_hash, right_res_hash, right_res_len)
        return (combined_hash, left_res_len + right_res_len)


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    precompute_powers(n)
    
    tree = SegmentTree(n, a)
    
    q = int(input())
    
    results = []
    for _ in range(q):
        t, l, r, k = map(int, input().split())
        
        if t == 0:
            tree.assign_range(l, r, k)
        elif t == 1:
            hash1, _ = tree.get_segment_hash(l, l + k - 1)
            hash2, _ = tree.get_segment_hash(r, r + k - 1)
            
            if hash1 == hash2:
                results.append('+')
            else:
                results.append('-')
            
    print(''.join(results))


if __name__ == "__main__":
    solve()
