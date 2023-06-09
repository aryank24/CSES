n = int(input())
t = sum(list(map(int, input().split())))
triangular = (n**2 + n) // 2
print(triangular - t)