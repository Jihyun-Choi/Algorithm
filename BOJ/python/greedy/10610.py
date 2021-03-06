N = input()

if "0" in N and sum(map(int, N)) % 3 == 0:  # 1
    print("".join(reversed(sorted(N))))  # 2
else:
    print(-1)

""" 10610
30의 배수가 되려면, 3의 배수이면서 일의 자리가 0인 수이다.
3의 배수는 각 자리 숫자의 합이 3의 배수인 수이다.

입력받은 N을 30의 배수로 만들려면 두 가지 조건을 만족해야한다.
1. 입력받은 수에 0이 존재한다.
2. 각 자리 숫자의 합이 3의 배수이다.

조건을 만족하면 각 숫자의 위치를 정렬하여 출력하고, 만족하지 않으면 -1을 출력하면 된다.

# 1
'if 문자 in 문자열'에서 문자열 안에 찾고자 하는 문자가 있을 시 True를 반환한다.
sum(map(int, N))은 문자열 N을 int타입으로 나눈 값으로 sum()함수를 사용해 합을 구한다.

# 2
문자열 자체를 정렬할 경우 "".join(sorted(문자열))을 사용한다.
sort() 함수는 리스트에서 사용되며, 문자열에서는 사용할 수 없다.
문자열에서 사용하고싶다면, sorted(문자열)로 사용 시 문자열이 리스트로 변환되어 정렬된다.
이를 join() 함수를 사용하여 리스트의 요소들을 문자열로 합친다.

정렬한 문자열을 역정렬하기위해 reversed() 함수를 사용하였다.
reverse() 함수도 동일하게 역정렬하지만, 반환값 없이 기존 리스트의 값을 변경한다.
"""
