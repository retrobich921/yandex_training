from math import log2


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    all_one = 0
    m = [[0] * 61 for _ in range(n)]
    mx_len = 0
    for i in range(n):
        cnt_one = 0
        q = 0
        while a[i] > 0:
            bit = a[i] & 1
            m[i][60 - q] = bit
            cnt_one += bit
            a[i] >>= 1
            q += 1
        mx_len = max(mx_len, q)
        all_one += cnt_one

    if all_one % 2 == 1:
        print('Impossible')
        return
    
    # print(mx_len)
    # for i in m:
    #     print(*i[61 - mx_len:])

    

if __name__ == "__main__":
    solve()
