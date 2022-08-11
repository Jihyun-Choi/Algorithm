N = int(input())
num = input().split()
num = list(map(int,a))
index = list()
for i in range(N):
    index.insert(num[N-1-i], N-i)
for j in index:
    print(j,end=' ')
