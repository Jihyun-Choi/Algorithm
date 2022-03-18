import sys

N = int(input())

for _ in range(N):
    quiz = list(sys.stdin.readline())
    sum = 0
    re = 1
    
    for i in quiz:
        
        if i == 'O':
            sum += re
            re += 1
        else :
            re = 1
    
    print(sum)
