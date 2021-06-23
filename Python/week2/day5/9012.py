# 괄호

a = int(input())

for i in range(a):
    b = input()
    s = list(b)     #입력받은 b를 리스트로 바꿔줌

    sum = 0         # 저장할곳

    for i in s :    # 리스트돌리기
        if i == '(':  
            sum += 1
        elif i == ')':
            sum -= 1       # 대칭을 맞추기위한 괄호 +-
        if sum < 0 
            print('NO')     # 0보다 클경우 남아있는 것이기때문에 no를 해주고 for문 빠지기
            break
    if sum > 0 :
        print('NO')
    elif sum == 0 :
        print('YES')