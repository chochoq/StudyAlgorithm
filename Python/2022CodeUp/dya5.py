
# 1. 영문자 1개 입력받아 10진수로 변환하기
n = ord(input())
print(n)


# 2. 정수 입력받아 유니코드 문자로 변환하기
c = int(input())
print(chr(c))

# 3. 정수 1개 입력받아 부호 바꾸기
n= input()
num = int(n)
if num > 0 :
    print(-num)
elif num == 0 :
    print(num)
else: print(-1 * num)

# 4. (6033)문자 1개 입력받아 다음 문자 출력하기
c = input()
printC = ord(c)+1
print(chr(printC))

# a를 숫자로 변환후 1일 더한뒤 다시 캐릭터로 변환한다

# 5. (6034) 정수 2개 입력받아 차 계산하기(설명)
a, b = input().split(' ')

c = int(a) - int(b)
print(c)


# 6. (6035) : [기초-산술연산] 실수 2개 입력받아 곱 계산하기
a, b = input().split(' ')

c = float(a) * float(b)
print(c)

# 7. (6036) : [기초-산술연산] 단어 여러 번 출력하기
a, b = input().split(' ')

c = a * int(b)
print(c)


# 8. (6037) 문장 여러 번 출력하기
n = input()
s = input()

print(int(n)*s)


# 9. (6038)  정수 2개 입력받아 거듭제곱 계산하기
a, b = input().split(" ")

c = int(a) ** int(b)

print(c)


# 10. (6039) 실수 2개 입력받아 거듭제곱 계산하기
a, b = input().split(" ")

c = float(a) ** float(b)

print(c)
