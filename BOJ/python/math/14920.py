n = int(input())
idx = 1
while n != 1:
    if n % 2:
        n = 3*n + 1
    else:
        n = n//2
    idx += 1
print(idx)
