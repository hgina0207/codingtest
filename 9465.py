T=int(input())

for t in range(T):
    n=int(input())
    board=[]
    dp=[[0]*n for _ in range(2)]
    for i in range(2):
        board.append(list(map(int,input().split())))
    dp[0][0]=board[0][0]
    dp[1][0]=board[1][0]
    if n>1:
        dp[0][1]=board[0][1]+board[1][0]
        dp[1][1]=board[1][1]+board[0][0]
    for j in range(2,n):
        dp[0][j]=board[0][j]+max(dp[1][j-2],dp[1][j-1])
        dp[1][j]=board[1][j]+max(dp[0][j-2],dp[0][j-1])

    print(max(dp[0][n-1],dp[1][n-1]))