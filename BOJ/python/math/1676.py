import math
N = int(input())
F = str(math.factorial(N))
num = 0
for i in F[::-1]:
    if i == "0":
        num += 1
    else:
        break
print(num)
