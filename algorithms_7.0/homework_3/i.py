from math import log2, ceil


def first():
    x = input()
    k = 0
    while k != ceil(log2(len(x) + k + 1)):
        k += 1
    a = [0] * (len(x) + k + 1)
    j = 0
    for i in range(1, len(a)):
        if log2(i) != int(log2(i)):
            a[i] = x[j]
            j += 1
    for i in range(k):
        cnt = 0
        for j in range(0, len(a), 2 ** (i + 1)):
            for k in range(j+2**i, j + 2 ** (i+1)):
                if k >= len(a):
                    break
                cnt += int(a[k])
        a[2**i] = 1 if cnt % 2 == 0 else 0
    for i in range(1, len(a)):
        print(a[i], end='')


def second():
    x = input()
    m_prime = len(x)
    a = [0] * (m_prime + 1)
    for i in range(m_prime):
        a[i+1] = int(x[i])

    error_pos = 0
    p = 1

    while p <= m_prime:
        current_sum = 0
        for j in range(1, m_prime + 1):
            if (j & p) != 0:
                current_sum += a[j]

        if current_sum % 2 == 0:
            error_pos += p

        p *= 2
    if error_pos > 0 and error_pos <= m_prime:
        a[error_pos] = 1 - a[error_pos] 

    x_recovered = []
    for i in range(1, m_prime + 1):
        is_power_of_2 = False
        if i > 0:
            if log2(i) == int(log2(i)):
                is_power_of_2 = True

        if not is_power_of_2:
             x_recovered.append(str(a[i]))

    print("".join(x_recovered))


def solve():
    q = int(input())
    if q == 1:
        first()
    else:
        second()

if __name__ == "__main__":
    solve()


'''
1
0100010000111101
'''