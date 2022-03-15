# 1
import sys 

C = int(input())

for _ in range(C):
    num = sys.stdin.readline().split()
    N = int(num[0])
    sum = cnt = 0
    
    for i in range(1,N+1):
        sum += int(num[i])
    sum = sum/N
    
    for i in range(1,N+1):
        if int(num[i]) > sum:
            cnt += 1
    
    rate = (cnt / N) * 100   
    
    print(f'{rate:.3f}%')

# 2
N = int(input())

for _ in range(N):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]  # 평균 구하기 (nums[0]: 학생수, nums[1:] 점수)
    cnt = 0
    
    for score in nums[1:]:
        if score > avg:
            cnt += 1  # 평균 이상인 학생 수
    rate = cnt/nums[0] *100
    
    print(f'{rate:.3f}%')
