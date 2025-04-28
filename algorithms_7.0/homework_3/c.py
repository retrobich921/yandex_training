def solve():
    n = int(input())
    a = list(map(int, input().split()))
    all_one = 0
    m = [[0, set(), _] for _ in range(n)]
    mx_len = 0
    for i in range(n):
        cnt_one = 0
        q = 0
        while a[i] > 0:
            bit = a[i] & 1
            cnt_one += bit
            m[i][0] += bit
            a[i] >>= 1
            q += 1
        mx_len = max(mx_len, q)
        all_one += cnt_one

    if all_one % 2 == 1:
        print('impossible')
        return
    
    i = 0
    cnt = mx_len * 2
    while cnt > 0:
        m.sort(key=lambda x: x[0], reverse=True)
        # print(all_one, m)
        if m[0][0] == 0:
            break
        # print(m)
        if i % mx_len not in m[0][1] and i % mx_len not in m[1][1]:
            m[0][0] -= 1
            m[0][1].add(i % mx_len)
            m[1][0] -= 1
            m[1][1].add(i % mx_len)
            all_one -= 2
            cnt = mx_len * 2
        cnt -= 1
        i += 1
        
    if all_one != 0:
        print('impossible')
    else:
        m.sort(key=lambda x: x[2])
        ans = []
        for i in range(n):
            q = list(m[i][1])
            t = 0
            for j in range(len(q)):
                t |= 1 << q[j]
            ans.append(t)
        print(*ans)


if __name__ == "__main__":
    solve()
