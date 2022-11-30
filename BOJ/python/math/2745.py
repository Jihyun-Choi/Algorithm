# 1
N, B = input().split()
arithmetic = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = 0
for i,n in enumerate(N[::-1]):
    answer += (int(B)**i) * (arithmetic.index(n))
print(answer)

# 2
number, notation = str(input()).split()
print(int(number,int(notation)))
