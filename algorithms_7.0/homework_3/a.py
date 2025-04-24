def solve():
    n = int(input())
    count = 0
    while n > 0:
        n &= (n - 1)
        count += 1
        
    print(count)



if __name__ == "__main__":
    solve()