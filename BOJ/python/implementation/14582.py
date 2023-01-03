A = list(map(int,input().strip().split()))
B = list(map(int,input().strip().split()))
a_sum, b_sum, flag = 0, 0, False
for i in range(9):
    a_sum += A[i]
    if a_sum > b_sum:
        flag = True
    b_sum += B[i]
print("Yes" if a_sum < b_sum and flag else "No")
