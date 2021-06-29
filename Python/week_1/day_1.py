# -*- coding: utf-8 -*-

# 최댓값 찾기
# 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.

# [3, 5, 6, 1, 2, 4]

# 이중for문

# def find_max_num(array):
#     for num in array:
#         for compare_num in array:
#             if num < compare_num:
#                 break
#         else:
#             return num


# 지정변수

def find_max_num(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num

    return max_num


print("정답 = 6 / 현재 풀이 값 = ")
print(find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ")
print(find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ")
print(find_max_num([6, 9, 2, 7, 1888]))
