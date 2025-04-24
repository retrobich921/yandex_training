def solve():
    n = int(input())
    used = [0] * n
    for i in range(n):
        a = list(map(int, input().split()))
        for j in range(n):
            i_j = a[j]
            if j > i and i_j > 0:
                used[i] |= i_j
                used[j] |= i_j

    print(*used)


if __name__ == "__main__":
    solve()
