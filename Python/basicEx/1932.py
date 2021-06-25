# import sys
# t = int(sys.stdin.readline())
# n=[list(map(int,sys.stdin.readline().split())) for _ in range(0,t)]
# dp=[]
# for i in range(1,t):
#     for j in range(len(n[i])):
#         if j == 0 :
#             n[i][j] += (n[i-1][j])
#         elif j==i:
#             n[i][j] +=(n[i-1][j-1])
#         else :
#             n[i][j] += (max(n[i-1][j],n[i-1][j-1]))
            
# print((n[t-1]))
# print(max(n[t-1]))
 

from sys import stdin
read = stdin.readline
lst = []
N = int(read())
for _ in range(N):
  lst.append(list(map(int, read().split())))
for i in range(1, N):
  for j in range(len(lst[i])):
    if j == 0:  # 배열 0번
      lst[i][j] += lst[i-1][j]
    elif j == len(lst[i])-1: # 가장 끝 배열
      lst[i][j] += lst[i-1][j-1]
    else:
      lst[i][j] += max(lst[i-1][j-1], lst[i-1][j]) #중간 배열들 
print(max(lst[N-1]))


# n = int(input())
# t = []
# for i in range(n):
#     t.append(list(map(int,input().split())))
#     # print(t)
# for i in range(1,n):
#     for j in range(i+1):
#         if j == 0 :
#             t[i][0] = t[i-1][0]+t[i][0] #왼쪽
#         elif i == j:
#             t[i][j] = t[i-1][j-1] + t[i][j] # 오른쪽 더할때
#             # print(t)
#         else:
#             t[i][j] = max(t[i-1][j-1]+t[i][j],t[i-1][j]+t[i][j])
#             # print(t)
# print(max(t[n-1]))