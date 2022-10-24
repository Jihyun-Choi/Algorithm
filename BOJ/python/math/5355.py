T = int(input())
for _ in range(T):
    case = list(input().split())
    num = float(case[0])
    for i in range(1, len(case)):
        if case[i] == '@':
            num *= 3
        elif case[i] == '%':
            num += 5
        elif case[i] == '#':
            num -= 7
    print("%0.2f" % num)
