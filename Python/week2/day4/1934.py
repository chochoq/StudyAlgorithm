# 최소공배수

# 최소 공배수를 구하는 방법은
# 최소 공배수를 구하고자 하는 두 수 A,B 그리고 그 수의 최대 공약수 C가 있다면
# A * B / C 로 답을 찾을 수 있다.

# import sys
# input = sys.stdin.readline

# a, b = map(int, input().split())

# def gcd_r(a, b):
#     return gcd_r(b, a % b) if b else a

# def gcd(a, b):
#     while b > 0:
#         tmp = a % b    # 큰수로 작은수를 나눔
#         a = b
#         b = tmp
#     return a

# def lcm(a, b):
#     return a * b // gcd(a, b)

# print(gcd_r(a, b))
# print(lcm(a, b))


n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    x = a
    y = b
    while b != 0:   # 0이 아니면 최대공약수를 구하는 식으로 들어간다
        r = a % b   # 큰수를 작은수로 나눈다(나머지를 구함)
        a = b       # 작은수 -> a
        b = r       # 나머지 -> b
    gcd = a         # 최대공약수
    lcd = x * y / a     # 최소공배수   A * B / C
    print(int(lcd))    # 최소공배수 출력



# 유클리드 호제법
# 큰수를 작은수로 나눈다
# 나머지는 작은수로, 작은수는 큰수로 바꿔준다음 
# 나머지가 0이 될 때 까지 반복해준다
# 나머지가 0이 될때의 작은 수가 최대공약수이다

# s = int(input('작은수 : '))
# b = int(input('큰수 : '))

# while True :    # 나머지가 0이 될 때 까지 반복해준다
#     r = b % s   # 큰수를 작은수로 나눈다
#     if r == 0 :  # 나머지가 0이 될때의 작은 수가 최대공약수이다
#         print('최대공약수는 ' , s)
#         break
#     # 나머지는 작은수로, 작은수는 큰수로 바꿔준다음 
#     b=s
#     s=r

