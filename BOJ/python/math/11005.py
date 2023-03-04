N, B = map(int, input().split())
notation = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = ''
while N != 0:
    answer += str(notation[N % B])
    N //= B
print(answer[::-1])
