# 타일

# n = int(input())
# dp=[0]*1000001
# dp[1]=1
# dp[2]=2

# for i in range(3,n+1):
#     dp[i]=(dp[i-1]+dp[i-2])%15746
# print(dp[n])


def tile(n):
    answer = 0
    tem_1=1
    tem_2=2
    for i in range(1,n+1):
        if i == 1 :
            answer = tem_1
        elif i == 2 :
            answer = tem_2
        else:
            answer = tem_1 + tem_2
            tem_1 = tem_2 % 15746
            tem_2 = answer % 15746

    print(answer % 15746)
tile(int(input()))