N = int(input())
cnt = 0
for _ in range(N):
    student, apple = map(int, input().split())
    cnt += apple % student
print(cnt)
