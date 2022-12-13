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

# 6053: [기초-논리연산] 참 거짓 바꾸기

a = bool(int(input()))
print(not a)

# 6054: [기초-논리연산] 둘 다 참일 경우만 참 출력하기
a, b = input().split()

print(bool(int(a)) and bool(int(b)))


# 6055 : [기초-논리연산] 하나라도 참이면 참 출력하기
a, b = input().split()

print(bool(int(a)) or bool(int(b)))


# 6056: [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기

a, b = input().split()

c = bool(int(a))
d = bool(int(b))

print((c and (not d) or ((not c) and d)))


# 6057 : [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기

a, b = input().split()

a = int(a)
b = int(b)

print(bool(a == b))


