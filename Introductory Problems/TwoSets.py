n = int(input())
triangular = n*(n+1) // 2
if triangular % 2 == 1:
    print("NO")
else:
    half_sum = triangular // 2
    set1, set2 = [], []
    for i in range(n, 0, -1):
        if i <= half_sum:
            set1.append(i)
            half_sum -= i
        else:
            set2.append(i)
    print("YES")
    print(len(set1))
    print(*set1)
    print(len(set2))
    print(*set2)
