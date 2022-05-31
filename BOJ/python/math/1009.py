import sys 
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a,b = map(int,input().split())
    a %= 10
    
    if a in [1, 5, 6]:
        print(a)
    elif a == 0:
        print(10)
    elif a in [4, 9]:
        b %= 2
        if b == 0:
            print(a*a%10)
        else:
            print(a)
    else:
        b %= 4
        if b == 0:
            print(a**4%10)
        else:
            print(a**b%10)
