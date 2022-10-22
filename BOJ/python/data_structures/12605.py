import sys
input = sys.stdin.readline
for i in range(int(input())):
    s = input().split()
    print(f'Case #{i+1}:', ' '.join(s[::-1]))
