import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    pair = []
    for i in range(1, n//2+1):
        if i == n-i: break
        pair.append(f"{i} {n-i}")
    print(f"Pairs for {n}: " + ", ".join(map(str, pair)))
