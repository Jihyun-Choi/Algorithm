# 1
N = int(input())
P = list(map(int, input().split()))

P.sort()

for i in range(1, N):
    P[i] += P[i-1]
print(sum(P))

# 2
n = int(input())
s = list(map(int, input().split()))
num = 0
s.sort()
for i in range(n):
    for j in range(i + 1):
        num += s[j]
print(num)

# 3
N = int(input())
P = list(map(int, input().split()))

P.sort()

answer = 0
for i in range(1, N+1):
    answer += sum(P[:i])

print(answer)

""" 11399
# 1로 구현하였다. 
# 2와 같은 경우에는 이중반복문으로 # 1보다 시간복잡도가 좋지않다.
"""
