N = list(map(int, input().split()))
x = min(N)
while True:
    cnt = 0
    for i in range(5):
        if x % N[i] == 0:
            cnt += 1
    if cnt > 2:
        print(x)
        break
    x += 1
