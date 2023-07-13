import sys
input = sys.stdin.readline
answer = 0
while True:
    money = int(input())
    if money < 0 :
        break
    answer += money
print(answer)
