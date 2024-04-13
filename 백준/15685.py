import sys
input=sys.stdin.readline
def make_dragon_curve(cur_gen,final_gen,dragon_x,dragon_y):
    global max_x,max_y,min_x,min_y
    if cur_gen==final_gen:
        return
    i=len(dragon_curve)-1
    while i>=0:
        direc=(dragon_curve[i]+1)%4
        dragon_curve.append(direc)
        dragon_x+=dx[direc]
        dragon_y+=dy[direc]
        if 0<=dragon_x<=100 and 0<=dragon_y<=100:
            board[dragon_y][dragon_x]=1
            max_x=max(max_x,dragon_x)
            max_y=max(max_y,dragon_y)
            min_x=min(dragon_x,min_x)
            min_y=min(dragon_y,min_y)
        i-=1
    make_dragon_curve(cur_gen+1,final_gen,dragon_x,dragon_y)
n=int(input())
board=[[0]*101 for _ in range(101)]
dragon_info=[]
max_x,max_y=0,0
min_x,min_y=0,0

dx=[1,0,-1,0]
dy=[0,-1,0,1]
for i in range(n):
    dragon_info.append(list(map(int,input().split())))
    max_x=max(dragon_info[i][0],max_x)
    max_y=max(dragon_info[i][1],max_y)
    min_x=min(dragon_info[i][0],min_x)
    min_y=min(dragon_info[i][1],min_y)

for i in range(n):
    dragon_curve=[dragon_info[i][2]]
    x=dragon_info[i][0]+dx[dragon_info[i][2]]
    y=dragon_info[i][1]+dy[dragon_info[i][2]]
    board[dragon_info[i][1]][dragon_info[i][0]]=1
    if 0<=x<=100 and 0<=y<=100:
        board[y][x]=1
    make_dragon_curve(0,dragon_info[i][3],x,y)


if min_x<0: min_x=0
if min_y<0: min_y=0

count=0
i=min_y
while i<=max_y:
    if i==100: break
    j=min_x
    while j<=max_x:
        if j==100: break
        if board[i][j]==1 and board[i][j+1]==1 and board[i+1][j]==1 and board[i+1][j+1]==1:
            count+=1
        j+=1
    i+=1


print(count)     



