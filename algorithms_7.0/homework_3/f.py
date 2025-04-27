def solve():
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(k)]

    xs = set()
    ys = set()
    zs = set()
    xy = set()
    xz = set() 
    yz = set()

    for xi, yi, zi in a:
        xy.add((xi, yi))
        xz.add((xi, zi))
        yz.add((yi, zi))

    full_xy = len(xy) == n * n
    full_xz = len(xz) == n * n
    full_yz = len(yz) == n * n

    if full_xy or full_xz or full_yz:
        print("YES")
    else:
        for x in range(1, n+1):
            for y in range(1, n+1):
                for z in range(1, n+1):
                    if (x, y) not in xy and (x, z) not in xz and (y, z) not in yz:     
                        print("NO")
                        print(x, y, z)
                        return
        print('YES')

if __name__ == '__main__':
    solve()
