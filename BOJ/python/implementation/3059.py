alphabet = {'A', 'B', 'C', 'D', 'E','F','G','H','I','J','K',
    'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
T = int(input())
for _ in range(T):
    S = set(input())
    alpha = alphabet - S
    sum = 0
    for i in alpha: 
        sum += ord(i)
    print(sum)
