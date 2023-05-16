T1 = float(input())
while True:
    T2 = float(input())
    if T2 == 999: break
    print("%.2f" % (T2-T1))
    T1 = T2
