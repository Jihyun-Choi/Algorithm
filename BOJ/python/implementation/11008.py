import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    s, p = map(str, input().split()) 
    cnt = s.count(p)
    word = s.replace(p, "")
    print(cnt + len(word))
