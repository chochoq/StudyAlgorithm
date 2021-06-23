# atm
# 각 사람이 돈을 인출하는데 필요한 합의 최솟값을 출력한다

n= int(input())
time = list(map(int,input().split()))
time.sort() 
# 시간이 적은 순서대로 정렬한다.
total=0
wait = 0

for i in time : # 정렬한 리스트로 반복
    wait += i
    # 걸린시간을 누적으로 더한다
    total += wait
    # 다음사람 순서의 시간을 반영

print(total)

# 원동균 / 27조 / 11399
# 그리드 알고리즘으로 최소시간 뽑기
# 꼼수를 써봅시다. 
# 이 문제에서 가장 최소시간이 걸리는 경우는 걸리는 시간인 P 배열값이 오름차순으로 정렬됐을 때 입니다.
# 따라서 p 배열을 정렬시키고, maxT라는 변수에 i값을 서서히 더해가며, t변수에는 maxT값을 더해가면 쉽게 최소시간을 구할 수 있습니다.

import sys

n = int(sys.stdin.readline().split()[0])
p = list(map(int, (sys.stdin.readline().split())))

p.sort()
t = 0
maxT = 0
for i in p :
    maxT += i 
    t += maxT

print(t)