N = int(input())

a = N//5

while a:
    mod = N - (a*5)
    if (mod % 3) == 0:
        b = mod//3
        break    
    a = a - 1

if (a == 0) and (N%3 == 0):
    print(N//3)
elif a == 0:
    print("-1")
else:
    print(a+b)
