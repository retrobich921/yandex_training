def solve():
    q = ['']
    array = []
    while q[0] != 'exit':
        q = input().split()
        if q[0] == 'push':
            n = int(q[1])
            array.append(n)
            print('ok')
        elif q[0] == 'pop':
            if len(array) != 0:
                print(array.pop())
            else:
                print('error')
        elif q[0] == 'back':
            if len(array) != 0:
                print(array[-1])
            else:
                print('error')
        elif q[0] == 'size':
            print(len(array))
        elif q[0] == 'clear':
            array.clear()
            print('ok')
        elif q[0] == 'exit':
            print('bye')


if __name__ == "__main__":
    solve()