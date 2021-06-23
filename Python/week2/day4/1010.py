# 다리놓기
# 이항계수로 왜풀어야하는가..?
# 조합, 경우의 수를 알아야하기때문?

from math import factorial

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    bridge = factorial(m)//(factorial(n) * factorial(m-n))
    print(bridge)


"# 원동균 / 27조 / 1010
# 위키백과의 이항계수 항목 정의 부분을 참조하였습니다.
# https://ko.wikipedia.org/wiki/%EC%9D%B4%ED%95%AD_%EA%B3%84%EC%88%98
# n => k , m => n 으로 보시면 됩니다~ 

import sys

t = int(sys.stdin.readline().split()[0])
arr = []

for i in range(t) :
    n, m = list(map(int, sys.stdin.readline().split()))

    mF = 1
    nF = 1
    mnF = 1
    for i in range(1, m + 1) :
        mF *= i

    for i in range(1, n + 1) :
        nF *= i

    for i in range(1, m - n+ 1) :
        mnF *= i
    arr.append(mF // (nF * mnF))

for i in arr :
    print(i)"