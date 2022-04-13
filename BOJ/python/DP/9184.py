import sys 
input = sys.stdin.readline 

def W(a,b,c):
    if a <= 0 or b<= 0 or c<=0: 
        return 1 
    if a > 20 or b > 20 or c > 20: 
        return W(20, 20, 20) 
    if dp[a][b][c]: 
        return dp[a][b][c] 
    if a<b<c: 
        dp[a][b][c] = W(a,b,c-1)+W(a,b-1,c-1)-W(a, b-1, c) 
        return dp[a][b][c] 
    dp[a][b][c] = W(a-1, b, c)+W(a-1,b-1,c)+W(a-1,b,c-1)-W(a-1,b-1,c-1) 
    return dp[a][b][c]
 
dp = [[[0]*(21) for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break    
    print(f'w({a}, {b}, {c}) = {W(a,b,c)}')

""" 9184
DP의 핵심은 반복이 되는 부분을 다시 반복하지 않는 것이다.
즉, 한번 계산한 값은 다시 계산하지 않도록하면 된다.
dq 리스트를 만들어 계산한 w()값을 저장한다.
"""
