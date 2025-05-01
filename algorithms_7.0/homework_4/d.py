def solve():
    n = int(input())
    apps = []
    for _ in range(n):
        q = input().split()
        if q[0] == 'Run':
            apps.append(' '.join(q[1:]))
            print(apps[-1])
        else:
            cnt_plus = q[0].count('+')
            print(apps[len(apps) - (cnt_plus % len(apps)) -1])
            apps.append(apps.pop(len(apps) - (cnt_plus % len(apps)) -1))


if __name__ == "__main__":
    solve()
