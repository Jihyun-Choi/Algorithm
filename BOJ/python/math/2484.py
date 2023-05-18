import sys
input = sys.stdin.readline

def reward(dice):
    if dice[0] == dice[3]:
        m = 50000 + dice[0] * 5000
    elif (dice[0] == dice[2]) or (dice[1] == dice[3]):
        m = 10000 + dice[1] * 1000
    elif (dice[0] == dice[1]) and (dice[2] == dice[3]):
        m = 2000 + (dice[0] + dice[2]) * 500
    elif (dice[0] == dice[1]) or (dice[1] == dice[2]):
        m = 1000 + dice[1] * 100
    elif dice[2] == dice[3]:
        m = 1000 + dice[2] * 100
    else:
        m = dice[3] * 100
    return m

N = int(input())
answer = []
for _ in range(N):
    dice = sorted(list(map(int, input().split())))
    answer.append(reward(dice))
print(max(answer))
