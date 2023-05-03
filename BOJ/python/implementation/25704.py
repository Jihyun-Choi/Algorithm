N = int(input())
P = int(input())
if N >= 20:
    print(min(max(0, P-2000), P*75//100))
elif N >= 15:
    print(min(max(0, P-2000), P*90//100))
elif N >= 10:
    print(min(max(0, P-500), P*90//100))
elif N >= 5:
    print(max(0, P-500))
else:
    print(P)
