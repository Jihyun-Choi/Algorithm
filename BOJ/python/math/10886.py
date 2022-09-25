N = int(input())
opinion = [int(input()) for _ in range(N)]
if opinion.count(1) > N//2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
