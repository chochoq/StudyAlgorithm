# -*- coding: utf-8 -*-

# Q.  다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오

# "hello my name is sparta"

def find_alphabet_array(string):
    # 알파벳의 숫자만큼 배열을 만들어줌
    alphabet_array = [0]*26

    return alphabet_array


result = find_alphabet_array

print("정답 = a 현재 풀이 값 =")
print(result("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =")
print(result("Sparta coding club"))
print("정답 = s 현재 풀이 값 =")
print(result("best of best sparta"))
