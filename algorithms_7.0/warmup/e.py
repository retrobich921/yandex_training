def solve(n):
    if n == 0:
        print(0)
        print(0, 0)
        return

    dp = [[0] * 101 for _ in range(101)]
    cnt = 0
    for i in range(1, n+1):
        if a[i] > 100:
            cnt += 1
            dp[i][cnt] = a[i] + dp[i-1][cnt-1]
        else:
            dp[i][cnt] = a[i] + dp[i-1][cnt]
        for j in range(cnt, -1, -1):
            dp[i][j] = min()
    return



n = int(input())
a = [0]
a += [int(input()) for _ in range(n)]
solve(n)

'''
5
35
40
101
59
63
'''