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
    n, m, k = map(int, input().split())
    for i in range(m):
        s = input()
    
    queries = []
    for i in range(k):
        q, u, v = input().split()
        u, v = int(u), int(v)
        if u > v:
            u, v = v, u
        queries.append((q, u, v))
    
    p = list(range(n + 1))
    rank = [0] * (n + 1)

    ans = []
    for i in range(k-1, -1, -1):
        q, u, v = queries[i]
        if q == "ask":
            if find_set(u, p) == find_set(v, p):
                ans.append("YES")
            else:
                ans.append("NO")
        else:
            unite_sets(u, v, p, rank)

    for i in range(len(ans)-1, -1, -1):
        print(ans[i])


if __name__ == "__main__":
    solve()
