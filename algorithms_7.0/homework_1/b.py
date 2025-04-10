def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []

    first = a[0]
    cnt = 1
    for i in range(1, n):
        if cnt + 1 <= min(first, a[i]):
            cnt += 1
            first = min(first, a[i])
        else:
            ans.append(cnt)
            first = a[i]
            cnt = 1
    ans.append(cnt)
    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()