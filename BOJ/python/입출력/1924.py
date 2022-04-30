X, Y = map(int, input().split())
Day = 0
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
for i in range(X-1):
    Day = Day + day[i]
print(week[(Day + Y) % 7])
