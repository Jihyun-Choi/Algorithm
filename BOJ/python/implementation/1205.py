N, score, P = map(int, input().split())
board = []
if N != 0:
    board = list(map(int, input().split())) + [score]
    board.sort(reverse=True)
    rank = board.index(score) + 1
    if rank > P:
        print(-1)
    else:
        if score == board[-1] and N == P:
            print(-1)
        else:
            print(rank)
else:
    print(1)
