n = int(input())
if n == 1:
    print(1)
elif n <= 3:
    print("NO SOLUTION")
else:
    i = 2 # print evens
    while i <= n:
        print(i, end=" ")
        i += 2  
    i = 1 # print odds
    while i <= n:
        print(i, end=" ")
        i += 2
