N = int(input())

for i in range(0,N):
    for k in range(0,i):
        print(" ", end="")
    for j in range(0,N-i):
        print("*", end="")
    print("")
