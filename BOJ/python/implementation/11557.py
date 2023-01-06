T = int(input())
for _ in range(T):
    school = []
    alchol = []
    N = int(input())
    for _ in range(N):
        x, y = map(str, input().split())
        school.append(x)
        alchol.append(int(y))
    print(school[alchol.index(max(alchol))])
