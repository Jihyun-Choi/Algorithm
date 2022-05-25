import sys
input = sys.stdin.readline
N, M = map(int, input().split())
X, Y = [], []
for _ in range(M):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()
if X[0] < Y[0]*6:
    answer = X[0] * (N//6) + Y[0] * (N%6)
    if X[0] < Y[0] * (N%6):
        answer = X[0] * (N//6 + 1)
else:
    answer = Y[0] * N
print(answer)

""" 1049
패키지 가격의 최솟값과 낱개 가격의 최솟값을 비교해 
패키지가 싸다면 패키지를 살 수 있는만큼 산 후에 낱개를, 낱개가 싸다면 전부 낱개로 구입하면 된다.  
주의할 부분은 패키지로 산 후 남은 개수를 낱개로 살 때, 낱개로 구입하는 가격이 패키지 하나의 가격보다 싸다면,
그냥 패키지를 하나 더 구입하는 것이 최솟값이다.
"""
