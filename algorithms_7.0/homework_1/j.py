def solve():
    n, d = map(int, input().split())
    items = [0] * n
    items[0] = [0, 0]
    max_cost = 0

    for i in range(n):
        name, cost = input().split()
        items[i] = [name, int(cost)]
        max_cost = max(max_cost, items[i][1])

    items.sort(key=lambda t: t[1])

    max_cost += 1
    ks = [-1] * max_cost
    ks[0] = 0

    names = []
    answer = 0
    for i in range(n):
        cost = -1
        # ищем минимальный способ избавиться от предметов в интервале now - d, now
        for j in range(max(0, items[i][1] - d), items[i][1] + 1):
            if ks[j] != -1:
                if cost != -1:
                    cost = min(cost, ks[j])
                else:
                    cost = ks[j]
        if cost == -1:
            continue
        cost += 1 # избавимся от нашего и вернем все предметы
        answer += cost
        names.append(items[i][0])
        for j in range(max_cost - items[i][1] - 1, -1, -1):
            if ks[j] != -1:
                if ks[j + items[i][1]] != -1:
                    ks[j + items[i][1]] = min(ks[j + items[i][1]], ks[j] + cost)
                else:
                    ks[j + items[i][1]] = ks[j] + cost

    names.sort()
    print(len(names), answer)
    print('\n'.join(names))


if __name__ == "__main__":
    solve()
