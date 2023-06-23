import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
	num = list(input())
	i = len(num)//2
	if num[i]==num[i-1]:
		print('Do-it')
	else: 
		print('Do-it-Not')
