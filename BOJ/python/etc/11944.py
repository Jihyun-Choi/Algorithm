N, M = map(int, input().split())
N_word = str(N)
NN = ''

while len(NN) < len(N_word) * N:
    NN += N_word
print(NN[:M])

""" map() 함수
map(적용시킬 함수, 적용할 값들) : 여러 개의 데이터를 한 번에 다른 형태로 변환하기 위해서 사용
-> 두 번째 인자로 들어온 반복 가능한 자료형(리스트나 튜플)을 첫 번째 인자로 들어온 함수에 하나씩 집어넣어서 함수를 수행

map 함수의 반환 값은 map객체 이기 때문에 해당 자료형을 list 혹은 tuple로 형 변환시켜야 한다.
"""
