var = [int(input()) for _ in range(5)]
if var[0] < 0:
    time = -var[0] * var[2] + var[3] + var[1] * var[4]
else:
    time = (var[1] - var[0]) * var[4]
print(time)
