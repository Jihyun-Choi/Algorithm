student = [list(map(str, input().split())) for _ in range(int(input()))]
student.sort(key=lambda x:(int(x[3]), int(x[2]), int(x[1])))
print(student[-1][0])
print(student[0][0])
