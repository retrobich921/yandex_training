n = int(input())
a = [0, 2, 4, 7]
dp = [0, 1, 2, 3]

if n < 4:
    print(a[n])
else:
    for i in range(n-3):
        dp.append(dp[-1] + dp[-2] + dp[-3])
        a.append(a[-1] + dp[-1])
    print(a[-1])