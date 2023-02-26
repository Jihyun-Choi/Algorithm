import sys
input = sys.stdin.readline

N = int(input())
candy = [list(map(str, input())) for _ in range(N)]
answer = 0

def check_row():
    global answer
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if candy[j][i] == candy[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            answer = max(answer, cnt)
def check_col():
    global answer
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if candy[j][i] == candy[j][i-1]:
                cnt += 1
            else:
                cnt = 1
            answer = max(answer, cnt)

for i in range(N):
    for j in range(N):
        if j < N-1:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            check_row()
            check_col()
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        if i < N-1:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            check_row()
            check_col()
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
print(answer)
