croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for i in croatia :
    word = word.replace(i, '*')
print(len(word))

""" 2941
리스트 안에 있는 요소를 순차적으로 돌 수 있는 반복문과, 문자열을 a에서 b로 바꿀 수 있는 replace()함수를 이용.
변경할 크로아티아 알파벳을 리스트에 담은 후 이 리스트를 반복문을 통해 입력받은 문자열에 리스트 요소가 있으면,
    이를 *로 바꾼 후 문자열의 길이를 출력한다.
"""
