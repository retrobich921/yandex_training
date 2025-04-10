def solve():
    n, M = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [-1] * (M+1)
    dp[0] = 0
    mx = -1
    for i in range(n):
        for j in range(M, a[i]-1, -1):
            if dp[j-a[i]] != -1:
                dp[j] = a[i]
                if j > mx:
                    mx = j
    print(mx)


if __name__ == "__main__":
    solve()