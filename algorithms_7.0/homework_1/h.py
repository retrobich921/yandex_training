def solve():
    # input
    n = int(input())
    orders = []
    is_any_odd = False

    for i in range(n):
        s = input()
        is_odd = len(s) % 2 == 1
        orders.append([0, 0, is_odd])
        is_any_odd = is_any_odd or is_odd
        for j in range(len(s)):
            if s[j] == "S":
                orders[i][j%2] += 1
        
    ans = 0
    if not is_any_odd:
        for order in orders:
            ans += order[0]
        print(ans)
    else:
        odd_orders = []
        for order in orders:
            if not order[2]:
                ans += max(order[0], order[1])
            else:
                odd_orders.append(order)

            odd_orders.sort(key=lambda x: x[0]-x[1])
            left = 0
            right = len(odd_orders) - 1
            step = 0
            while left <= right:
                if step == 1:
                    ans += odd_orders[left][1]
                    left += 1
                else:
                    ans += odd_orders[right][0]
                    right -= 1
                step = 1 - step
        print(ans)


if __name__ == "__main__":
    solve()
