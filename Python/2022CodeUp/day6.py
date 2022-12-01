# 1) 6040: [기초-산술연산] 정수 2개 입력받아 나눈 몫 계산하기

a, b=input().split(" ")
c = int(a) // int(b)
print(c)


# 2) 6041 : [기초-산술연산] 정수 2개 입력받아 나눈 나머지 계산하기

a, b = input().split(" ")
c = int(a) % int(b)
print(c)

# 3) 6042 : [기초-값변환] 실수 1개 입력받아 소숫점이하 자리 변환하기

f = input()
f = float(f)
print(format(f,".2f"))


# 4) 6043 : [기초-산술연산] 실수 2개 입력받아 나눈 결과 계산하기

f1, f2 = input().split(" ")
f = float(f1) / float(f2)
print(format(f, ".3f"))


# 5) 6044: [기초-산술연산] 정수 2개 입력받아 자동 계산하기

a, b = input().split(" ")

a = int(a)
b = int(b)

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a % b)
print(format(a/b, ".2f"))


# 6) 6045 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기
a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

plus = a + b + c
pun = plus / 3
print(plus , format(pun,".2f"))


# 7) 6046 : [기초-비트시프트연산] 정수 1개 입력받아 2배 곱해 출력하기

a = input()

a = int(a)
print(a << 1)


# 8) 6047 [기초-비트시프트연산] 2의 거듭제곱 배로 곱해 출력하기(설명)(py)

a, b = input().split()

a = int(a)
b = int(b)

print(a << b)


# 9) 6048 : [기초-비교연산] 정수 2개 입력받아 비교하기1

a, b =input().split()

a = int(a)
b = int(b)
if a < b:
    print("True")
elif a >= b:
    print("False")


# 10) 6049 : [기초-비교연산] 정수 2개 입력받아 비교하기2
a, b = input().split()

a = int(a)
b = int(b)
if a == b:
    print("True")
elif a != b:
    print("False")
