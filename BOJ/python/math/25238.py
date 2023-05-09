A, B = map(int, input().split())
print(0 if (A - (B/100 * A)) >= 100.0 else 1)
