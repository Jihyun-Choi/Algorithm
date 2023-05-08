# 1 
def solution(n): 
    answer = 1
    num = [i+1 for i in range(n)]
    i, j = 0, 1
    while i< n and j != n:  # if i == n-1 and j == n : break
        if sum(num[i:j]) == n: answer += 1
        if sum(num[i:j]) <= n : j += 1
        else : i += 1
        print(i, j, answer)
    return answer

# 2
def solution(n):
    answer = 0
    for i in range(1, n+1):
        sum_val = 0
        for j in range(i, n+1):
            sum_val += j
            if sum_val == n:
                answer += 1
            elif sum_val > n:
                break
    return answer
