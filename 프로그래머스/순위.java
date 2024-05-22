class Solution {
    public int solution(int n, int[][] results) {
        int[][] res=new int[n+1][n+1];
        for(int[] r:results){
            int a=r[0];
            int b=r[1];
            res[a][b]=1;
            res[b][a]=-1;
        }
        for(int m=1;m<=n;m++){
            for (int s=1;s<=n;s++){
                for (int e=1;e<=n;e++){
                    if (res[s][m]==1 && res[m][e]==1) res[s][e]=1;
                    else if (res[s][m]==-1 && res[m][e]==-1) res[s][e]=-1;
                }
            }
        }
        int answer = 0;
        for(int i=1;i<=n;i++){
            int cnt=0;
            for (int j=1;j<=n;j++){
                if(res[i][j]!=0) cnt++;
            }
            if(cnt==n-1) answer++;
        }
        
        return answer;
    }
}