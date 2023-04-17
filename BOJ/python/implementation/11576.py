A, B = map(int,input().split())
m = int(input())
arr = list(map(int,input().split()))
sum = 0
for i in range(m):
    sum += arr[-i-1]*(A**i)
result = []
while sum//B:
    result.append(sum%B)
    sum = sum//B
result.append(sum)
result.reverse()
print(*result)
