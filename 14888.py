import sys
import itertools
input=sys.stdin.readline
def dfs(depth,res,plus,minus,multiply,divide):
    global max_num,min_num
    if depth==n:
        max_num=max(res,max_num)
        min_num=min(res,min_num)
    
    if plus: dfs(depth+1,res+num[depth],plus-1,minus,multiply,divide)
    if minus: dfs(depth+1,res-num[depth],plus,minus-1,multiply,divide)
    if multiply: dfs(depth+1,res*num[depth],plus,minus,multiply-1,divide)
    if divide: dfs(depth+1,int(res/num[depth]),plus,minus,multiply,divide-1)


n=int(input())
num=list(map(int,input().split()))
oper=list(map(int,input().split()))

max_num=-1e9
min_num=1e9

dfs(1,num[0],oper[0],oper[1],oper[2],oper[3])

print(max_num)
print(min_num)