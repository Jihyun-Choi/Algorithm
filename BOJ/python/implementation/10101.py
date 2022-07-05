X = int(input())
Y = int(input())
Z = int(input())
if (X + Y + Z) == 180:
    if X == Y == Z == 60:
        print("Equilateral")
    elif X == Y or Y == Z or Z == X:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
