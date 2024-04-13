import sys
n,m=map(int,sys.stdin.readline().split())

board=[]
for _ in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))

max_num=0
hap=0

for i in range(n):
    for j in range(0,m,4):
        if m-j>=4:
            for k in range(4):
                if j+k+3>=m: break    
                hap=board[i][j+k]+board[i][j+k+1]+board[i][j+k+2]+board[i][j+k+3]
                if max_num<hap: max_num=hap
        if m-j>=3:
            for k in range(4):
                if j+k+2>=m: break
                hap=board[i][j+k]+board[i][j+k+1]+board[i][j+k+2]
                if i+1<n:
                    for l in range(3):
                        hap+=board[i+1][j+k+l]
                        if max_num<hap: max_num=hap
                        hap-=board[i+1][j+k+l]
        if m-j>=2:
            for k in range(4):
                if j+k+1>=m: break
                hap=board[i][j+k]+board[i][j+k+1]
                if i+1<n:
                    for l in range(-1,2):
                        if j+k+l>=0 and j+k+l+1<m:
                            hap+=board[i+1][j+k+l]+board[i+1][j+k+l+1]
                            if max_num<hap: max_num=hap
                            hap-=(board[i+1][j+k+l]+board[i+1][j+k+l+1])
                if i+2<n:
                    for l in range(2):
                        hap+=board[i+1][j+k+l]+board[i+2][j+k+l]
                        if max_num<hap: max_num=hap
                        hap-=(board[i+1][j+k+l]+board[i+2][j+k+l])
        if m-j>=1:
            for k in range(4):
                if j+k>=m: break
                if i+3<n:
                    hap=board[i][j+k]+board[i+1][j+k]+board[i+2][j+k]+board[i+3][j+k]
                    if max_num<hap: max_num=hap
                if i+2<n:
                    hap=board[i][j+k]+board[i+1][j+k]+board[i+2][j+k]
                    for l in range(-1,2):
                        if (l==-1 and j+k!=0) or (l==1 and j+k+l<m):
                            hap+=board[i+1][j+k+l]
                            if max_num<hap: max_num=hap
                            hap-=board[i+1][j+k+l]
                            hap+=board[i+2][j+k+l]
                            if max_num<hap: max_num=hap
                            hap-=board[i+2][j+k+l]
                    
                    hap=board[i][j+k]+board[i+1][j+k]
                    if j+k-1>=0:
                        hap+=board[i+1][j+k-1]+board[i+2][j+k-1]
                        if max_num<hap: max_num=hap
                        hap-=board[i+1][j+k-1]+board[i+2][j+k-1]
                    if j+k+1<m:
                        hap+=board[i+1][j+k+1]+board[i+2][j+k+1]
                        if max_num<hap: max_num=hap
                        hap-=board[i+1][j+k+1]+board[i+2][j+k+1]
                if i+1<n:
                    hap=board[i][j+k]+board[i+1][j+k]
                    if j+k-2>=0:
                        hap+=board[i+1][j+k-2]+board[i+1][j+k-1]
                        if max_num<hap: max_num=hap
                        hap-=board[i+1][j+k-2]+board[i+1][j+k-1]
                    if j+k-1>=0 and j+k+1<m:
                        hap+=board[i+1][j+k-1]+board[i+1][j+k+1]
                        if max_num<hap: max_num=hap
                        hap-=board[i+1][j+k-1]+board[i+1][j+k+1]
                    if j+k+2<m:
                        hap+=board[i+1][j+k+1]+board[i+1][j+k+2]
                        if max_num<hap: max_num=hap
                        hap+=board[i+1][j+k+1]+board[i+1][j+k+2]
print(max_num)