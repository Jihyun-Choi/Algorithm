N = int(input())
C = [int(input()) for _ in range(N)]
C.sort(reverse=True)  
result=0
for i in range(2, len(C), 3):
  result += C[i]
print(sum(C)-result)
