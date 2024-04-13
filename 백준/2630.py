import sys
input=sys.stdin.readline
n=int(input())
paper=[]
b,w=0,0
def solution(x,y,n):
    global b,w
    color=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color!=paper[i][j]:
                solution(x,y,n//2)
                solution(x,y+n//2,n//2)
                solution(x+n//2,y,n//2)
                solution(x+n//2,y+n//2,n//2)
                return
    if color==0: w+=1
    else: b+=1
for _ in range(n):
    paper.append(list(map(int,input().split())))

solution(0,0,n)
print(w)
print(b)