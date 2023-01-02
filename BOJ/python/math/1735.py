import math
A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())
numerator = A1 * B2 + A2 * B1
denominator = B1 * B2
common = math.gcd(numerator, denominator)
numerator //= common
denominator //= common
print(numerator, denominator)
