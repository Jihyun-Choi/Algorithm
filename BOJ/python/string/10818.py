N = int(input())

num = list(map(int, input().split()))
print("%d %d" % (min(num), max(num)))

""" 10818
두 번째 줄에서 입력받은 정수들을 공백단위로 구분하여 int형으로 리스트 num에 할당한다.
리스트의 최솟값과 최댓값을 min(), max() 함수를 사용하여 출력한다.
"""
