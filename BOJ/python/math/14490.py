def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

N, M = map(int, input().split(':'))
mod = gcd(N, M)
print(f"{N//mod}:{M//mod}")
