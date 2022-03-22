import sys

N = int(input())
word = []

for i in range(0,N):
    word.append(sys.stdin.readline().strip())

word = list(set(word))  # 1

word.sort()
word.sort(key = len)

for i in word:
    print(i)


""" #1
set()은 집합 자료형으로 중복을 허용하지 않는다.
주로 중복을 제거하기 위한 필터 역할로 사용된다.
같은 단어가 여러번 입력된 경우에는 한 번만 출력되도록 중복을 제거하였다.
"""

"""
오류...
for i in range(0,N):
    word[i] = sys.stdin.readline()
"""
