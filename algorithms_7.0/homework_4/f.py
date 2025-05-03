def solve():
    n = int(input())
    a = [0] + list(int(input()) for i in range(n))
    used = [False] * (n + 1)
    ans = 0

    for i in range(1, n+1):
        if used[i]:
            continue
        
        if a[i] == i:
            ans += 1
            used[i] = True
        else:
            race = set()
            while not used[i]:
                used[i] = True
                race.add(i)
                i = a[i]
            if i in race:
                ans += 1

    print(max(ans, 1))


if __name__ == "__main__":
    solve()
