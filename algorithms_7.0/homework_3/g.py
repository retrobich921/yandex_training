def f(i):
    return i & (i + 1)


def add(i, x, t):
    while i < len(t):
        t[i] += x
        i = i | (i + 1)


def summa(l, r, t):
    return pref(r, t) - pref(l - 1, t)


def pref(r, t):
    res = 0
    while r >= 0:
        res += t[r]
        r = f(r) - 1
    return res


def solve():
    n, k = map(int, input().split())
    t = [0] * (n + 2)
    a = [0] * (n + 2)

    for _ in range(k):
        q = input().split()
        if q[0] == 'A':
            i = int(q[1])
            x = int(q[2])
            delta = x - a[i]
            a[i] = x
            add(i, delta, t)
        else:
            l = int(q[1])
            r = int(q[2])
            print(summa(l, r, t))


if __name__ == "__main__":
    solve()