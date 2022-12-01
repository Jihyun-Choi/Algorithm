S = input()
for i in S:
    if 'a'<=i<='z':
        print(chr(97 + (ord(i)+13-97) % 26), end='')
    elif 'A'<=i<='Z':
        print(chr(65 + (ord(i)+13-65) % 26), end='')
    else:
        print(i, end='')
