import sys
input = sys.stdin.readline
index = 0
while True:
    n0 = int(input())
    if n0 == 0: break
    index += 1
    n1 = 3*n0
    n2 = (n1+1)//2 if n1%2 else n1//2
    n3 = 3*n2
    n4 = n3//9
    if n0 == 2*n4:
        print(f"{index}. even {n4}")
    else:
        print(f"{index}. odd {n4}")
