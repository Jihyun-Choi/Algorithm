N = int(input())
T = list(map(int, input().split()))
T.sort(reverse=True)
for i in range(len(T)):
    T[i] = T[i] + i + 2
print(max(T))
