def solve():
    n = int(input())
    ln = len(bin(n)) - 2
    ans = n
    q = int('1' * ln, 2)
    for i in range(16):
        n = ((n << 1) & q) | (n >> (ln - 1))
        ans = max(ans, n)
    print(ans)


if __name__ == "__main__":
    solve()
