# 제로

count = int(input())
stack = []

for i in range(count):
    num = int(input())
    if(num==0):         #num이 0이면 pop 해주기
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))