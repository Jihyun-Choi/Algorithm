T = int(input())
for _ in range(T):
    N = int(input())
    sum_c = 0
    sum_g = 0
    for _ in range(N):
        C, G = map(float, input().split())
        sum_c += C
        sum_g += C * G
    GPA = sum_g / sum_c
    print(int(sum_c), '%.1f' % GPA)
