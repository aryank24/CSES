t = int(input())
for _ in range(t):
    r, c = list(map(int, input().split()))
    maxrc = max(r,c)
    diag_val = maxrc*maxrc - (maxrc-1)
    if r==c:
        print(diag_val)
    elif r>c:
        if r % 2 == 0:
            print(diag_val + (r-c))
        else:
            print(diag_val - (r-c))
    else:
        if c % 2 == 1:
            print(diag_val + (c-r))
        else:
            print(diag_val - (c-r))