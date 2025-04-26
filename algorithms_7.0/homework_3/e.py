def solve():
    x, y = map(int, input().split())
    
    xx, c = map(int, input().split())

    print(x ^ y)
    print(xx ^ c)

if __name__ == "__main__":
    solve()


'''
example:
input:
3 4
5 23

ответ для первого примера:
матрица
4, 5, 6, 7, 0
3, 2, 1, 0, 7
2, 3, 0, 1, 6
1, 2, 3, 2, 5
0, 1, 2, 3, 4

и ответ будет 7, потому что 7 лежит на (3, 4)

правильные ответы:
output:
7
18

'''