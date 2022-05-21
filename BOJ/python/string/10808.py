word = list(map(lambda x: ord(x)-97, input().strip()))
alpha = [0]*26
for i in word:
    alpha[i] += 1
print(*alpha)

""" 10808
입력받은 문자열을 아스키코드값으로 변환하여 소문자 'a'의 아스키코드 값인 97을 뺀 후 리스트로 저장한다.
그 후 리스트를 반복문을 통해 존재하는 개수만큼 +1 하여 저장 후 출력한다.
print(*리스트)는 리스트의 요소를 띄어쓰기 기준으로 출력해준다.
"""
