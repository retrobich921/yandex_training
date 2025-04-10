n, m = map(int, input().split())
x = list(map(lambda i_v: [i_v[0], int(i_v[1])], enumerate(input().split()))) # [[ind, value]]
y = list(map(lambda i_v: [i_v[0], int(i_v[1])], enumerate(input().split()))) # [[ind, value]]

x.sort(key=lambda x: x[1], reverse=True)
y.sort(key=lambda x: x[1], reverse=True)

cnt = 0
j = 0
for i in range(m):
    while j < n and x[j][1] + 1 > y[i][1]:
        x[j][1] = 0
        j += 1
    if j == len(x):
        break
    cnt += 1
    x[j][1] = y[i][0] + 1
    j += 1

x.sort()
print(cnt)
for i in x:
    print(i[1], end=" ")