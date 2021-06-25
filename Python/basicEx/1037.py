# 약수
# 가장 작은 값과 가장 큰 값을 곱하면
# 진짜수를 구할수있다.

# n = int(input())
# a = list(map(int,input().split()))
# a_max = max(a)    # 최댓값을 구함
# a_min = min(a)    # 최솟값을 구함
# print(a_max*a_min)    # 최대와 최소를 곱함


import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

a.sort()    #sort를 시켜 정렬을 시켜준
print(a[0] * a[-1]) # 배열 0과 -1을 구해(최대,최솟값) 곱함
