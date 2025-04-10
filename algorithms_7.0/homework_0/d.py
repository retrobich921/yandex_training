n, m = map(int, input().split())

a = [[0] * (m + 1) for _ in range(n+1)]

for i in range(1, n+1):
    q = [0] + list(map(int, input().split()))
    for j in range(1, m + 1):
        a[i][j] = max(a[i-1][j], a[i][j-1]) + q[j]

# for i in a:
#     print(i)

ans = []

# print(n, m)
while n > 0 and m > 0:
    # print(a[n][m-1], a[n-1][m])
    if a[n][m-1] > a[n-1][m]:
        ans += ['R']
        m -= 1
    else:
        ans += ['D']
        n -= 1

# print(ans)
print(a[-1][-1])
for i in range(len(a) + len(a[0]) - 4):
    print(ans[-2-i], end=' ')