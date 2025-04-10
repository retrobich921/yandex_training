def f(M, i, a):
    if i == 30:
        return 0
    cnt = 0
    if M % a[i][2] == 0:
        cnt += M // a[i][2] * a[i][1]
        return cnt
    
    cnt += M // a[i][2] * a[i][1]
    M = M % a[i][2]
    cnt += min(a[i][1], f(M, i+1, a))
    return cnt


def solve():
    M = int(input())
    a = list(map(lambda x: [(1<<x[0]) / int(x[1]), 1<<x[0], int(x[1])], enumerate(input().split()))) # [cost/time, cost, sec]
    a.sort()
    cnt = f(M, 0, a)
    print(cnt)


if __name__ == "__main__":
    solve()