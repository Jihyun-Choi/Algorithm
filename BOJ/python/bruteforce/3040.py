# 1
dwarf = [int(input()) for _ in range(9)]
flag = False
for i in range(8):
    if flag:
        break
    for j in range(i+1, 9):
        if sum(dwarf) - dwarf[i] - dwarf[j] == 100:
            dwarf.pop(i)
            dwarf.pop(j-1)
            print(*dwarf, sep='\n')
            flag = True
            break

# 2
dwarf = [int(input()) for _ in range(9)]
def find():
    for i in range(8): 
        for j in range(i+1, 9):
            if sum(dwarf) - dwarf[i] - dwarf[j] == 100:
                dwarf.pop(i)
                dwarf.pop(j-1)
                print(*dwarf, sep='\n')
                return
find()

""" 3040
# 1 34044 KB	72 ms
# 2 30840 KB	72 ms

| 다중반복문 빠져나가기
# 1 flag를 활용한 다중 반복문 탈출
# 2 함수 내부의 return을 통한 반복문 탈출

| 리스트에서 요소를 삭제할 때, pop del
- pop : 삭제 후 삭제한 요소 반환
- del : 반환없이 요소 삭제
    del str_list[3:]과 같이 여러개의 요소를 한꺼번에 삭제 가능 
반환여부의 차이로 del이 pop보다 수행속도가 빠름

위 문제에서 pop대신 del 사용 시 실행시간이 4ms 느림 (?)
"""
