import sys

num = int(input())

for i in range(0, num):
    A, B = map(int, sys.stdin.readline().split())
    print(f"Case #{i+1}: {A} + {B} = {A+B}")
    