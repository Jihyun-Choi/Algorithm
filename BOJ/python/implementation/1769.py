X = input()
cnt = 0
while len(X) > 1:
    X = str(sum(map(int, list(X))))
    cnt += 1
print(cnt)
print("YES" if int(X) % 3 == 0 else "NO")
