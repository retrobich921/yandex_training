def solve(n):
    if n == 0:
        print(0)
        print(0, 0)
        return

    dp = [[-1] * 101 for _ in range(n + 1)]
    from_day = [[-1] * 101 for _ in range(n + 1)]
    use_coupon = [[False] * 101 for _ in range(n + 1)]

    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(101):
            if dp[i - 1][j] == -1:
                continue

            price = a[i]

            # обед за деньги
            new_coupons = j + 1 if price > 100 else j
            new_cost = dp[i - 1][j] + price

            if dp[i][new_coupons] == -1 or new_cost < dp[i][new_coupons]:
                dp[i][new_coupons] = new_cost
                from_day[i][new_coupons] = j
                use_coupon[i][new_coupons] = False

            # используем купон
            if j > 0:
                if dp[i][j - 1] == -1 or dp[i - 1][j] < dp[i][j - 1]:
                    dp[i][j - 1] = dp[i - 1][j]
                    from_day[i][j - 1] = j
                    use_coupon[i][j - 1] = True

    min_cost = -1
    coupons_left = 0
    for j in range(101):
        if dp[n][j] != -1 and (min_cost == -1 or dp[n][j] < min_cost or (dp[n][j] == min_cost and j > coupons_left)):
            min_cost = dp[n][j]
            coupons_left = j

    used = []
    cur_coupons = coupons_left
    for i in range(n, 0, -1):
        if use_coupon[i][cur_coupons]:
            used.append(i)
        cur_coupons = from_day[i][cur_coupons]

    used.sort()
    print(min_cost)
    print(coupons_left, len(used))
    for day in used:
        print(day)


n = int(input())
a = [0] + [int(input()) for _ in range(n)]
solve(n)


'''
5
35
40
101
59
63

5
101
105
150
76
120
'''