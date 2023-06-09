import sys
input = sys.stdin.readline
jinho = input()
MBTI = [input() for _ in range(int(input()))]
print(MBTI.count(jinho))
