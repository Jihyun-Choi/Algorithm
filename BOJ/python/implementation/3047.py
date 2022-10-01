num = sorted(list(map(int, input().split())))
order = list(input())
for i in order:
    if i == "A":
        print(num[0], end=" ")
    elif i == "B":
        print(num[1], end=" ")
    else:
        print(num[2], end=" ")
