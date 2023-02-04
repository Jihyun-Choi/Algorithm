import sys
sudoku = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]
blank = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def check(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(9):
        if a == sudoku[x][i]:
            return False
        if a == sudoku[i][y]:
            return False
    for i in range(3):
        for j in range(3):
            if a == sudoku[nx+i][ny+j]:
                return False
    return True

def dfs(cnt):
    if cnt == len(blank):
        for i in range(9):
            print(*sudoku[i])
        exit(0)

    for i in range(1, 10):
        x = blank[cnt][0]
        y = blank[cnt][1]

        if check(x, y, i):
            sudoku[x][y] = i
            dfs(cnt+1)
            sudoku[x][y] = 0
dfs(0)
