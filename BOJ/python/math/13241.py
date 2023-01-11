def gcd(x, y):
    if x<y:
        x, y = y, x
    while y :
        x, y = y, x%y
    return x

A, B = map(int, input().split())
print(A * B // gcd(A, B))
