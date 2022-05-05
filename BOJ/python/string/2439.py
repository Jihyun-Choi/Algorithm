N = int(input())

for i in range(0,N):
    for k in range(0,N-1-i):
        print(" ", end="")
    for j in range(0,i+1):
        print("*", end="")
    print("")
