import copy


def solve():
    N, M = map(int, input().split())
    m = list(map(int, input().split()))
    c = list(map(int, input().split()))
    bag = [[[-1, -1] for _ in range(M+1)] for _ in range(N+1)] #[[[ind_object, cost], [-1, -1], ..., [-1, -1]], [], []]
    bag[0][0] = [0, 0]
    ind_mx = 0
    for i in range(1, N+1):
        bag[i] = copy.deepcopy(bag[i-1]) # копируем предыдущие состояния, чтобы потом восстановить дорогу
        for j in range(M, m[i-1]-1, -1):
            if bag[i][j-m[i-1]][1] != -1: # цена не равняется -1, то есть там был какой то объект или там ничего не лежит
                if bag[i][j][1] < bag[i][j-m[i-1]][1] + c[i-1]:
                    bag[i][j] = [i, bag[i][j-m[i-1]][1] + c[i-1]]
                    if bag[i][j][1] > bag[i][ind_mx][1]:
                        ind_mx = j

    ans = []
    i = bag[N][ind_mx][0]
    while ind_mx > 0:
        ans += [bag[i][ind_mx][0]]
        i = bag[i][ind_mx][0] - 1
        ind_mx -= m[ans[-1]-1]

    print(*reversed(ans), sep='\n')


if __name__ == "__main__":
    solve()
