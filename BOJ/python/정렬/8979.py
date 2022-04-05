import sys
input = sys.stdin.readline

N, K = map(int, input().split())

s = []
for i in range(N):  
    s.append(list(map(int, input().split())))

s.sort(key=lambda x : (-x[1], -x[2], -x[3]))
for i in range(N):  # 문제에서 주어진 나라 K의 인덱스 값 찾기
    if s[i][0] == K:
        index = i
for i in range(N):
    if s[index][1:] == s[i][1:]:
        print(i + 1)
        break

""" 8979
s 리스트의 각 요소는 입력받은 리스트이다.
즉, s[0] = [1, 3, 0, 0], s[1] = [3, 0, 0, 2], ... 이다.

key 매개변수를 가지는 sort() 함수는 key 값을 기준으로 정렬되고 기본값은 오름차순이다. 또한 lambda식을 사용할 수 있다.
key 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬하며, -를 붙이면 현재 정렬차순과 반대로 하게 된다.
"""
