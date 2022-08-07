T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    paper = [0 for _ in range(N)]
    paper[M] = 1
    cnt = 0
    while True:
        if P[0] == max(P):
            cnt += 1
            if paper[0] == 1:
                print(cnt)
                break
            else:
                del P[0]
                del paper[0]
        else:
            P.append(P[0])
            del P[0]
            paper.append(paper[0])
            del paper[0]
