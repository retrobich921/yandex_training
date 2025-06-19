def update(t, size, x, y, z, add):
    i = x
    while i < size:
        row_i = t[i]
        j = y
        while j < size:
            col_ij = row_i[j]
            k = z
            while k < size:
                col_ij[k] += add
                k = k | (k + 1)
            j = j | (j + 1)
        i = i | (i + 1)


def query(t, x, y, z):
    res = 0
    i = x
    while i > 0:
        row_i = t[i]
        j = y
        while j > 0:
            col_ij = row_i[j]
            k = z
            while k > 0:
                res += col_ij[k]
                k = (k & (k + 1)) - 1
            j = (j & (j + 1)) - 1
        i = (i & (i + 1)) - 1
    return res


n = int(input())
size = n + 1
t = [[[0] * size for _ in range(size)] for _ in range(size)]
out = []

while True:
    data = input().split()
    m = int(data[0])
    if m == 1:
        x, y, z, add = map(int, data[1:])
        x += 1
        y += 1
        z += 1
        update(t, size, x, y, z, add)
    if m == 2:
        x1, y1, z1, x2, y2, z2 = map(lambda x: int(x) + 1, data[1:])
        total = (
            query(t, x2, y2, z2)
            - query(t, x1 - 1, y2, z2)
            - query(t, x2, y1 - 1, z2)
            - query(t, x2, y2, z1 - 1)
            + query(t, x1 - 1, y1 - 1, z2)
            + query(t, x1 - 1, y2, z1 - 1)
            + query(t, x2, y1 - 1, z1 - 1)
            - query(t, x1 - 1, y1 - 1, z1 - 1)
        )
        out.append(str(total))
    if m == 3:
        break

print("\n".join(out))
