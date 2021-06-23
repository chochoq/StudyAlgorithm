# 통계학
# https://www.acmicpc.net/problem/2108

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

# 첫째 줄에는 산술평균을 출력한다. 
# 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 둘째 줄에는 중앙값을 출력한다.
# 셋째 줄에는 최빈값을 출력한다. 
# 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 넷째 줄에는 범위를 출력한다.



import sys

n = int(sys.stdin.readline())
list = []

# 산술평균
n = n//n+i

# 중앙값

n = 

# 최빈값
cnt = 

# 범위
min()-max()



"# 원동균 / 27조 / 2108
# 평균값, 중간값, 최빈값, 범위값 중에서 최빈값이 가장 구현이 힘들었어서 최빈값만 설명합니다.
# 1 ~ len(arr)만큼 반복문을 수행하면서 전값과 현재 값이 다를 때 cnt 값이 maxNum보다 크면 maxNum = cnt를 하고 maxVal 배열을 초기화 하며, 배열에 추가해줍니다.
# 배열을 초기화 하는 이유는 최대값이 새로 갱신되면 이전 값이 필요없기 때문입니다.
# 만약에 같은 값을 찾으면 한번 더 배열에 추가해줍니다.
# 반복문이 끝나면 아직 arr[-1]에 대한 cnt값이 잔여해 있으므로 이제 이 값과 배열들의 값과 비교해줍니다.
# 같다면 2번째 최빈값이기 때문에 그냥 maxVal[1]을 반환하면 됩니다.
# 아니라면 arr[-1]값을 반환해줍니다.

import sys

n = int(sys.stdin.readline().split()[0])

def algAvg() :
    avg = 0
    sum = 0
    for i in arr :
        sum += i

    avg = round(sum / len(arr), 0)
    return int(avg)


def algMid() :
    L = 0
    R = len(arr) - 1
    m = (L + R) // 2
    return arr[m]

def algMin() :
    maxVal = []
    maxNum = 0
    cnt = 1
    for i in range(1, len(arr)) :
        if arr[i - 1] != arr[i] :
            if cnt > maxNum :
                maxNum = cnt
                maxVal.clear()
                maxVal.append(arr[i-1])
            elif cnt == maxNum :
                maxVal.append(arr[i-1])
            cnt = 1
        else :
            cnt += 1
    if cnt > maxNum :
        return arr[-1]
    elif cnt == maxNum :
        maxVal.append(arr[-1])
    
    if len(maxVal) == 1 :
        return maxVal[0]
    else :
        return maxVal[1]

def algMinus() :
    maxNum = max(arr)
    minNum = min(arr)

    return maxNum - minNum


arr = []
for i in range(n) :
    num = int(sys.stdin.readline().split()[0])
    arr.append(num)

arr.sort()
print(algAvg())
print(algMid())
print(algMin())
print(algMinus())"
