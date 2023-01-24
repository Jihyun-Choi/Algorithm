N = int(input())
x = int(input()) 
vote = [int(input()) for _ in range(N-1)]
count = 0  
vote.sort(reverse=True) 
if N == 1:
  print(0)
else:
  while vote[0] >= x:
    x += 1
    vote[0] -= 1
    count += 1
    vote.sort(reverse=True)
  print(count)
