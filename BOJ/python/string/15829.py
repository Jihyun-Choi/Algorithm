L = int(input())
string = input()
M, r = 1234567891, 31
answer = 0
for i in range(len(string)):
    answer += (ord(string[i]) - 96) * (r ** i)
print(answer % M)
