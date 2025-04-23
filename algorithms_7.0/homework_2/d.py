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
        size = len(self.tree) >> 1
        for i in range(size - 1, 0, -1):
            left = self.tree[i << 1]       # ребёнок 2*i
            right = self.tree[i << 1 | 1]  # ребёнок 2*i+1
            if right[0] > left[0]:
                self.tree[i] = right.copy()
            elif right[0] < left[0]:
                self.tree[i] = left.copy()
            else:
                # при равенстве берём значение + индекс левого
                self.tree[i] = [left[0], left[1]]

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
        # не пересекаются
        if r <= left or right <= l:
            return [-float("inf"), 0]

        if l <= left and right <= r:
            return self.tree[node]
        mid = (left + right) >> 1
        L = self.query_ind_max(node << 1, left, mid, l, r)
        R = self.query_ind_max(node << 1 | 1, mid, right, l, r)
        if R[0] > L[0]:
            return R
        elif R[0] < L[0]:
            return L
        else:
            # при равенстве возвращаем индекс из левой части
            return [L[0], L[1]]

    def upgrade_max(self, ind, value):
        self.tree[ind] = [value, ind - (len(self.tree) >> 1) + 1]
        # протягиваем вверх
        self.upgrade_max_ind(ind)

    def upgrade_max_ind(self, ind):
        """Рекурсивно обновляем родителей, если они стали меньше потомка."""
        parent = ind >> 1
        if parent == 0:
            return
        left = self.tree[parent << 1]
        right = self.tree[parent << 1 | 1]
        # выбираем лучший из двух детей (левая сторона при равенстве)
        if right[0] > left[0]:
            best = right
        else:
            best = left
        # если родитель уже равен best — можно остановиться
        if self.tree[parent] == best:
            return
        self.tree[parent] = best.copy()
        # идём дальше вверх
        self.upgrade_max_ind(parent)


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