# 영화감독숌
# 입력받은 수의 -1해서 +666붙이면 안됨?

import time
start_time = time.time()

n = int(input())
cnt = 0
six_n = 666
while True :
    if '666' in str(six_n): # six_n안에 666이 포함되면 
        cnt += 1          # cnt에 1을 증가
        print(six_n)
    if cnt == n :         # n이 cnt랑 같으면 탈출
        print(six_n)
        break
    six_n +=1

##################

# n = int(input())
# m = 666
# while(n) :
#     if '666' in str(m):
#         n -= 1
#         print(m)
#     m += 1

# print(m-1)



end_time = time.time()
print("time: ", end_time - start_time)