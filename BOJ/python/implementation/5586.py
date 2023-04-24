string = input()
X, Y = 0, 0
for i in range(len(string)-2):
    answer = ''.join(string[i:i+3])
    if answer == 'JOI': X += 1
    if answer == 'IOI': Y += 1
print(X, Y, sep="\n")
