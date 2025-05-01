from collections import deque


def solve():
    queue = deque()
    q = ['']
    while q[0] != 'exit':
        q = input().split()
        if q[0] == 'push_front':
            n = int(q[1])
            queue.appendleft(n)
            print('ok')
        elif q[0] == 'push_back':
            n = int(q[1])
            queue.append(n)
            print('ok')
        elif q[0] == 'pop_front':
            if len(queue) != 0:
                print(queue.popleft())
            else:
                print('error')
        elif q[0] == 'pop_back':
            if len(queue) != 0:
                print(queue.pop())
            else:
                print('error')
        elif q[0] == 'front':
            if len(queue) != 0:
                print(queue[0])
            else:
                print('error')
        elif q[0] == 'back':
            if len(queue) != 0:
                print(queue[-1])
            else:
                print('error')
        elif q[0] == 'size':
            print(len(queue))
        elif q[0] == 'clear':
            queue.clear()
            print('ok')
        elif q[0] == 'exit':
            print('bye')


if __name__ == "__main__":
    solve()