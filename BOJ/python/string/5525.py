# 1
N = int(input())
M = int(input())
S = input()
Pn = 'IO'*N + 'I'
cnt = 0 
for i in range(M - len(Pn)):
    if Pn == S[i:i+len(Pn)]:
        cnt += 1
print(cnt)

# 2
N = int(input())
M = int(input())
S = input() 
answer, i, cnt = 0, 0, 0
while i < (M - 1):
    if S[i:i+3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == N:
            answer += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0
print(answer)
