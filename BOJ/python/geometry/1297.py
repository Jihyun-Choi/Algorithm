D, H, W = map(int, input().split())
R = D / ((H ** 2 + W ** 2) ** (1 / 2))
print(int(H * R), int(W * R))
