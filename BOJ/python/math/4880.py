import sys
input = sys.stdin.readline
while True:
    a1, a2, a3 = map(int, input().split())
    if a1 == a2 == a3 == 0: break
    if a3 == 2 * a2 - a1:
        print("AP", 2*a3 - a2)
    else:
        print("GP", int(a3 * (a3/a2)))

""" 4880
입력이 많은 경우에는 readline을 쓰면 시간을 절반정도 감소.
"""
