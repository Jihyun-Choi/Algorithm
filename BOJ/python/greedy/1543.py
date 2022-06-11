A = input()
B = input()
cnt, i = 0, 0
while i <= (len(A)-len(B)):
    if A[i:i+len(B)] == B:
        cnt += 1
        i += len(B)
    else:
        i += 1
print(cnt)
