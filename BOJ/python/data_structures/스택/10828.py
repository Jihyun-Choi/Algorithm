import sys


N = int(input())
stack = []

for _ in range(N):  # 1
    order = sys.stdin.readline().split()
    
    if order[0] == "push":
        stack.append(order[1])
        
    elif order[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
            
    elif order[0] == "size":
        print(len(stack))
        
    elif order[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
            
    elif order[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])


""" 10828
파이썬은 stack 구조를 제공하지 않는다.
기본 클래스 list를 이용하여 stack을 표현할 수 있다.

반복적인 입력이 많은 경우에는 input()함수를 지양한다는 사실을 잊지말자!
"""

""" # 1
파이썬에서 _는 몇몇의 경우에 사용이 된다. 해당 코드에서 _는 "값을 무시하고 싶은 경우"이다.
보통 for 변수 in ... 과 같이 변수를 둔다.
위의 문제에서는 for문 안에서 사용할 특정 변수가 있는 것이 아닌, 단순히 반복을 위한 반복문이다.
따라서 사용하지 않는 변수를 설정하는 것이 아닌, _를 작성하므로써 변수를 설정하지 않더라도 오류가 발생하지 않는다.
"""

""" STACK이란?
STACK(스택) : LFIO(Last In First Out)
    기다란 상자안에 물건을 넣고 빼는 것을 상상하면 쉽게 이해할 수 있다.

사용 사례 : 웹 브라우저 방문기록(뒤로가기), 실행 취소, 역순 문자열 만들기, 후위 표기법 계산
"""