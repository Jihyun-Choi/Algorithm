# 1 
def dfs():  # 깊이 우선 탐색
    if len(permut) == N:
        print(*permut)
        return
    for i in range(1, N+1):
        if i not in permut:
            permut.append(i)
            dfs()
            permut.pop()

N = int(input())
permut = []
dfs()

# 2 : 라이브러리 사용
from itertools import permutations
N = int(input())
number = [i for i in range(1, N+1)]
for numbers in list(permutations(number)):
    print(*numbers)
