n = int(input())
t = [1] * (n+1)
for i in range(1, n+1):
    t[i] = 0
    for j in range(i):
        t[i] += t[j] * t[i-j-1]      
print(t[n])
