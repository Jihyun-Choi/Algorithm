# 1
def gcd(x,y):
    if y == 0:
        return x
    return gcd(y, x % y)
A, B = map(int, input().split())
print('1' * gcd(A, B))


# 2
def gcd(x, y):
    mod = x % y
    while mod >0:
        x = y
        y = mod
        mod = x % y
    return y
