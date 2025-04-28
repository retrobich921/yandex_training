from math import log2


def int2q(n) -> tuple[int, str]:
    k = n >> 5
    letter = chr(n & 0b11111 + ord('a'))
    return k, letter


def q2int(letter, k) -> int:
    letter = ord(letter) - ord('a')
    return (k << 5) | letter


def pack():
    s = input()
    encode = []
    zip = [''] * 8
    letters = dict()
    # for i in range(len(s)):

    print(len(encode))
    print(*encode)


def unpack():
    n = int(input())
    a = list(map(int, input().split()))
    s = ''

    print(s)


def solve():
    q = input()
    if q == 'pack':
        pack()
    else:
        unpack()

if __name__ == '__main__':
    solve()
