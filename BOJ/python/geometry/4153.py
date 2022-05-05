while True:
    X, Y, Z = map(int, input().split())
    if X == Y == Z == 0:
        break
    X *= X
    Y *= Y
    Z *= Z
    if X+Y == Z or Y+Z == X or X+Z == Y :
        print("right")
    else:
        print("wrong")
