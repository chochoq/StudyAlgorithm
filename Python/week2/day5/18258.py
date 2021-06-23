# 큐 2
# https://www.acmicpc.net/problem/18258

#push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 
# 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.


import sys
from collections import deque

n = int(sys.stdin.readline())
deque = deque()

def push(queque, x):            # x를 큐에 넣는다
    deque.append(x)

def pop(deque):         
    if not deque:               # 들어있는 것이없으면 -1출력
        return -1
    else :
        return deque.popleft()  # 큐에서 가장앞에 있는 정수를 빼고 수출력

def size():                     #큐에 들어있는 정수의 개수를 출력한다.
    return len(deque)

def empty():
    if not deque:               #큐가 비어있으면 1, 아니면 0을 출력한다.
        return 1
    else :
        return 0

def front():            
    if not deque :              # 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        return -1
    else:
        return deque[0]        #큐의 가장 앞에 있는 정수를 출력한다

def back():
    if not deque :             # 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        return -1
    else :              
        return deque[-1]        #큐의 가장 뒤에 있는 정수를 출력한다.

for i in range(n):
    oper = sys.stdin.readline().split()
    if(oper[0]=="push"):
        push(deque,oper[1])
    elif(oper[0]=="pop"):
        print(pop(deque))
    elif(oper[0]=="size"):
        print(size())
    elif(oper[0]=="empty"):
        print(empty())
    elif(oper[0]=="front"):
        print(front())
    elif(oper[0]=="back"):
        print(back())