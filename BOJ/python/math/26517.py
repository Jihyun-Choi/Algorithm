k = int(input())
a, b, c, d = list(map(int, input().split()))
left = a*k + b
right = c*k + d
print("Yes", left) if left == right else print("No")
