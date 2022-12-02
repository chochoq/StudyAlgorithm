# 6050: [기초-비교연산] 정수 2개 입력받아 비교하기3

a, b =input().split()

a = int(a)
b = int(b)

if a <= b :
    print(True)
else: print(False)


# 6051 : [기초-비교연산] 정수 2개 입력받아 비교하기4

a, b = input().split()

a = int(a)
b = int(b)

if a != b:
    print(True)
else:
    print(False)


# 6052 : [기초-논리연산] 정수 입력받아 참 거짓 평가하기

a = int(input())
print(bool(a))
