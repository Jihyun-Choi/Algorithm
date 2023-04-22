N = list(map(int, input()))
A, B = 0, 0
for i in range(len(N)//2):
    A += N[i]
    B += N[-(i+1)] 
print("LUCKY") if A == B else print("READY")
