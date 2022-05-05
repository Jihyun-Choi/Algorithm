# input은 입력되는 모든 것을 문자열로 취급한다.
   
num = input().split()  # 입력받은 문자열의 공백 제거 
print(int(num[0])+int(num[1]))  # 인덱스를 활용해 int() 함수로 정수로 형 변환 후 합산

A, B = input().split()	# input()함수로 입력받은 문자열을 split() 함수로 나누어 A,B 변수에 저장
print(int(A)+int(B))	# int() 함수로 A와 B를 정수로 형 변환 후 합산
