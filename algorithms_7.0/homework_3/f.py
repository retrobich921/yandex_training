import sys


def solve():
    n, k = map(int, sys.stdin.readline().split())
    log_block = 10
    bits_in_block = 1 << log_block
    cnt_blocks = (n + bits_in_block - 1) >> log_block
    xy = [[False] * n for _ in range(n)]
    xz = [[0] * cnt_blocks for _ in range(n)]
    yz = [[0] * cnt_blocks for _ in range(n)]

    for i in range(k):
        x, y, z = map(int, sys.stdin.readline().split())
        x, y, z = x - 1, y - 1, z - 1
        xy[x][y] = True
        z_block = z >> log_block
        z_pos = z & (bits_in_block - 1)
        z_set = 1 << z_pos
        xz[x][z_block] |= z_set
        yz[y][z_block] |= z_set
    last_bits = (cnt_blocks << log_block) - n
    last_block_filler = ((1 << last_bits) - 1) << (bits_in_block - last_bits)
    for i in range(n):
        xz[i][cnt_blocks - 1] |= last_block_filler
        yz[i][cnt_blocks - 1] |= last_block_filler
    full_block_mask = (1 << bits_in_block) - 1
    for x in range(n):
        for y in range(n):
            if not xy[x][y]:
                for block in range(cnt_blocks):
                    if xz[x][block] | yz[y][block] != full_block_mask:
                        now_pos = 1
                        for i in range(bits_in_block):
                            if (xz[x][block] | yz[y][block]) & now_pos == 0:
                                ans = (x+1, y+1, (block << log_block) + i + 1)
                                if ans[2] <= n:
                                    print('NO')
                                    print(*ans)
                                    return
                                break
                            now_pos <<= 1
    print('YES')


if __name__ == '__main__':
    solve()
