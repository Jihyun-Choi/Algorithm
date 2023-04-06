y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
answer = [y2-y1-1, y2-y1+1, y2-y1]
if m1 < m2:
    answer[0] = y2-y1
elif m1 == m2 and d1 <= d2:
    answer[0] = y2-y1
for i in answer : print(i)
