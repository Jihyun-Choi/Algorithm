M = int(input())
N = int(input())
num = []
for i in range(M,N+1):
    if i == 1:
        pass
    elif i == 2:
        num.append(i)
    else:
        for j in range(2, i):
            if i%j == 0:
                break
            elif j == i-1:
                num.append(i)
if len(num) == 0:
    print('-1')
else:
    print(sum(num))
    print(min(num))
