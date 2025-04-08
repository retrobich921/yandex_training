import sys


sys.setrecursionlimit(10**7)
def dfs(node, parent):
    ans[node] = 1

    if node in tree.keys():
        for i in tree[node]:
            if i != parent:
                dfs(i, node)
                ans[node] += ans[i]
            # print(ans)


v = int(input())
tree = dict()
ans = [0] * (v)
for i in range(v-1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if x in tree.keys():
        tree[x] += [y]
    else: tree[x] = [y]
    if y in tree.keys():
        tree[y] += [x]
    else: tree[y] = [x]

dfs(0, -1)

print(*ans)
