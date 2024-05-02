from collections import deque
import sys
sys.setrecursionlimit(10**6)
def solution(land):
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    global cnt
    def dfs(i,j,num):
        global cnt
        land[i][j]=num
        visited[i][j]=True
        for k in range(4):
            ny=i+dy[k]
            nx=j+dx[k]
            if 0<=nx<len(land[0]) and 0<=ny<len(land) and not visited[ny][nx] and land[ny][nx]==1:
                cnt+=1
                dfs(ny,nx,num)
    
    oil_num={}
    visited=[[False]*len(land[0]) for _ in range(len(land))]
    num=1
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j]!=0 and not visited[i][j]:
                cnt=1
                dfs(i,j,num)
                oil_num[num]=cnt
                num+=1   
    max_get=0
    for i in range(len(land[0])):
        get=0
        oil_visited=[]
        for j in range(len(land)):
            if land[j][i]!=0 and land[j][i] not in oil_visited:
                get+=oil_num[land[j][i]]
                oil_visited.append(land[j][i])
            
        max_get=max(get,max_get)       
    return max_get