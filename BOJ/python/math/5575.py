for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    t = (h2-h1)*60*60 + (m2-m1)*60 + s2-s1
    h = t//60//60 % 24
    m = t//60 % 60
    s = t%60
    print(h, m, s)