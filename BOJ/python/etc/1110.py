# 1
def cycle(n):
    if n<10:
        n = n*10
    num = str(n)
    n = ((int(num[0]) + int(num[1])) % 10) + (int(num[1]) * 10)
    return int(n)


N = int(input())
sum = 0
num = N

while True:
    val = cycle(num)
    if N == val:
        break
    sum += 1
    num = val

print(sum)


# 2
N = int(input())
sum = 0
num = N

while True:
    num = cycle(num)
    sum += 1
    if num == N:
        break

print(sum)

# 3 
N = int(input())
sum = 0
num = N

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c
    
    sum += 1
    if num == N:
        break

print(sum)
    
    
