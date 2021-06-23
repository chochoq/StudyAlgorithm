# # 팩토리얼 사용법

# #내장함수이용
# import math

# print(math.factorial(5))

# print(math.factorial(20))


# # 단순반복문
# # n부터 1까지 곱해서 반복문을 통해 늘려나간다
# def factorial_for(n):
#     ret = 1
#     for i in range(1, n+1):
#         ret *= i
#     return ret
# print(factorial_for(5))
# print(factorial_for(20))


# # 재귀함수

# def factorial_recursive(n):
#     return n* factorial_recursive(n-1) if n > 1 else 1
#     #삼항연산자사용

# print(factorial_recursive(5))
# print(factorial_recursive(20))


# 반복문
# s = 0
# for i in  [100,200,300, 400]:
#     s += i
# print(s)

# 재귀함수
# def s(l):
#     if len(l) == 1:
#         return l[0]         # langs가 1일때 0번 배열을 리턴
#     else :                  # langs가(리스트) 2이상이면 0번 배열 + 1부터 마지막까지 슬라이싱한 값을 더한다
#         return l[0]+s(l[1:])
# print(s([100,200,300, 400]))


print(2**6) # 2의 6제곱 64
# for  문
result = 1
for i in range(6):
    result *= 2
print(result)

# 함수

#재귀


# def f(n):
#     if n <= 1:
#         return 1
#     else :
#         return n*(n-1)

# print(f(3))



# def f(n):
#     if n == 0 or n==1:
#         return 1
#     return f(n-1) * f(n-2)

# print(f(3))