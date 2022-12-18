import sys
input = sys.stdin.readline 
N = int(input())
expected = [int(input()) for _ in range(N)]
expected.sort()
sum = 0
for i in range(1, N+1):
    sum += abs(i-expected[i-1])
print(sum)
