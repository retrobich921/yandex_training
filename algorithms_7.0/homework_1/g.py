def solve():
    # input
    N, K = map(int, input().split())
    bricks = [[] for _ in range(K + 1)]
    for i in range(N):
        l, c = map(int, input().split())
        bricks[c].append(l)

    # problem solving
    bag = [[[] for _ in range(5001)] for _ in range(K+1)]
    # for i in range(1, K+1):



if __name__ == "__main__":
    solve()
