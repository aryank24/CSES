dna = input()
curr, long = 1, 1
for i in range(1, len(dna)):
    if dna[i-1] == dna[i]: 
        curr += 1
    else: 
        curr = 1
    long = max(curr, long)
print(long)
