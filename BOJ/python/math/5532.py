import math
val = [int(input()) for _ in range(5)]
print(val[0] - max(math.ceil(val[1] / val[3]), math.ceil(val[2] / val[4])))
