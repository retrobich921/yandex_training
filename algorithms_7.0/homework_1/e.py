def solve():
    N, M = map(int, input().split())
    m = list(map(int, input().split()))
    c = list(map(int, input().split()))
    dp = [-1] * (M+1)
    dp[0] = 0
    mx = 0
    for i in range(N):
        for j in range(M, m[i]-1, -1):
            if dp[j-m[i]] != -1:
                dp[j] = max(dp[j], dp[j-m[i]] + c[i])
                if dp[j] > mx:
                    mx = dp[j]
    print(mx)


if __name__ == "__main__":
    solve()