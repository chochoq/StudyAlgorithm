# 이진탐색
def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1

    while start_index <= end_index:

        mid_index = (start_index + end_index) // 2

        if some_list[mid_index] == element:
            return mid_index
        elif some_list[mid_index] > element:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1

    return None

# 선형탐색
def linear_search(element, some_list):
    for i in range(len(some_list)):
        if some_list[i] == element:
            return i
    return None


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))