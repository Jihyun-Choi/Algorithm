import sys
input = sys.stdin.readline
A = []
N = int(input())
for _ in range(N):
    a,b,c,d = list(map(str,input().split()))
    A.append( [a, int(b),int(c),int(d)])
A.sort(key = lambda x : (-x[1] , x[2],-x[3],x[0]) )
for i in A :
    print(i[0])
