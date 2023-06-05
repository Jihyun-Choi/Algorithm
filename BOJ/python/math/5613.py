import sys
input = sys.stdin.readline
answer = int(input())
while True:
    op = input().rstrip()
    if op == '=':
        break
    n = int(input())
    if op == '+': answer += n;
    elif op == '-': answer -= n;
    elif op == '*': answer *= n;
    elif op == '/': answer //= n;
print(answer)
