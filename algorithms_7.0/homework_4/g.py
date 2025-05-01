import sys


def find_set(v, parent):
    if v == parent[v]:
        return v
    parent[v] = find_set(parent[v], parent)
    return parent[v]


def unite_sets(a, b, parent, rank):
    a = find_set(a, parent)
    b = find_set(b, parent)
    if a != b:
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1
        return True
    return False


def solve():
    n, m = map(int, sys.stdin.readline().split())
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    num_components = n
    ans = -1
    for i in range(1, m + 1):
        u, v = map(int, sys.stdin.readline().split())
        if ans != -1:
            continue
        if unite_sets(u, v, parent, rank):
            num_components -= 1
        if num_components == 1:
            ans = i
    print(ans)


if __name__ == "__main__":
    solve()
