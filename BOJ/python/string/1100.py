Chess = [list(map(str, input())) for _ in range(8)]
cnt = 0
for i in range(4):
    for j in range(4):
        if Chess[2*i][2*j] == 'F':
            cnt += 1
        if Chess[2*i+1][2*j+1] == 'F':
            cnt += 1
print(cnt)
