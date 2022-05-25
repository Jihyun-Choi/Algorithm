W = input()
word = [W[i::] for i in range(len(W))]
word.sort()
print(*word, sep='\n')

""" 11656
리스트 앞에 *을 적으면 요소를 공백 기준으로 출력한다.
공백 기준이 아닌 엔터 기준으로 하고싶다면 sep='\n'을 적는다.
"""
