while True:
    N = input()
    if N == '0':
        break 
    cnt = 0
    for i in list(N):
        if i == '0':
            cnt += 5
        elif i == '1':
            cnt += 3
        else:
            cnt += 4
    print(cnt+1)
