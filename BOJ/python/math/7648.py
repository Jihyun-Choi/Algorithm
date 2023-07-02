import sys
for i in sys.stdin.readlines():
    n, k = map(int, i.strip().split())
    t, answer = 0, 0
    while n >= k:
        t = n//k
        answer += k*t
        n = n%k+t
    answer += n
    print(answer)
