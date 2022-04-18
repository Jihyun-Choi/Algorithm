import sys 
N, K = map(int, sys.stdin.readline().split())

item = [[0, 0]] 
for i in range(1, N + 1): 
    item.append(list(map(int, sys.stdin.readline().split()))) 
dp = [[0] * (K + 1) for _ in range(N + 1)]  # (N+1) x (K+1) matrix 
for i in range(1, N + 1):  # 물건을 한개씩 배열을 채워나감
    for j in range(1, K + 1):  # 하나의 물건을 1부터 K까지 무게를 차례차례 비교
        if j >= item[i][0]:  # 해당 인덱스(i번째)의 물건의 무게가 j보다 작거나 같을 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-item[i][0]] + item[i][1]) 
        else:  # 해당 인덱스(i번째)의 물건의 무게가 j보다 큰 경우, 가방에 담을 수 없음.
            dp[i][j] = dp[i-1][j]
print(dp[N][K])

""" 12865
item 리스트에 물건 하나의 무게와 가치를 리스트로 추가한다.
dp리스트는 [물건의 개수 x 넣을수있는 무게] 이다.
dp리스트를 1열부터 N열까지 각각 1부터 k까지 값을 비교하며 채워나간다.
채워나가는 방식은 무게가 j일 경우 해당 인덱스의 물건의 무게와 비교해 담을 수 있는지의 여부를 판단한다. 
즉, dp[i][j]는 i번째 물건까지 가방에 담았을 때, 무게가 j인 경우의 가치의 최댓값이다.  (1<=i<=N, 1<=j<=K) 
i값과 j값을 하나씩 늘려가며 dp리스트를 채워 구하고자 하는 가방에 담을 수 있는 가치의 최댓값인 dp[N][K]를 구한다. 

담을 수 없다면 dp리스트의 이전 인덱스(dp[i-1][j])의 값을 그대로 할당하고, 
담을 수 있다면 dp리스트의 이전 인덱스의 해당 무게 값(dp[i-1][j])과 
    담을 수 있는 무게에서 물건의 물건을 뺀 값의 가치(dp[i-1][j-item[i][0]])에서 해당 물건의 가치를 더한 값과 비교하여 최댓값을 할당한다.
"""
