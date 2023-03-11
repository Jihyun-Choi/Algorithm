# 1  내 풀이
import sys
input = sys.stdin.readline
N, C = list(map(int, input().split()))
home = [int(input()) for _ in range(N)]
home.sort()
start, end = 1, home[-1]-home[0]
answer = 0 
while(start <= end):
    mid = (start + end) // 2  # 공유기 사이의 거리 초기값 설정
    flag = home[0]  # 공유기 위치
    cnt = 1  # 설치한 공유기 개수
    for i in range(1, N):
        if home[i] >= flag + mid:
            flag = home[i]  # 공유기를 설치
            cnt += 1
    if cnt >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)

# 2  다른 사람 풀이
import sys
input = sys.stdin.readline
N, C = list(map(int, input().split()))
home = [int(input()) for _ in range(N)]
home.sort()
lo, hi = 1, (home[-1]-home[0])//(C-1)
while lo <= hi:
    mid = (lo+hi)//2
    start, cnt = home[0], 1
    for temp in home[1:]:
        if temp-start >= mid:
            cnt+=1
            start=temp
    if cnt >= C:
        lo=mid+1
    else:
        hi=mid-1
print(hi)


""" 2110
구하고자 하는 공유기 사이의 거리를 이분탐색 아이디어를 사용해 탐색하는 방법.
각 공유기의 위치를 이분탐색하는 것이 아닌, 공유기 사이의 거리를 이분탐색하는 것이 핵십.
"""
