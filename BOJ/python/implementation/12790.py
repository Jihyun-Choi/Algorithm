import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))
    hp = (arr[0]+arr[4] if arr[0]+ arr[4]>=1 else 1)
    mp = (arr[1]+arr[5] if arr[1]+arr[5]>=1 else 1)
    at = (arr[2]+arr[6] if arr[2]+arr[6]>=0 else 0)
    print(hp + mp*5 + 2*at + (arr[3]+arr[7])*2)
