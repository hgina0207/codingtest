class Solution {
    public int solution(int n) {
        long[] dp=new long[n+1];
        int mod=1000000007;
        dp[1]=2;
        dp[2]=3;
        for (int i=3;i<=n;i++){
            if (i%2!=0){
                dp[i]=dp[i-1]*2+dp[i-2];
            }else{
                dp[i]=dp[i-1]+dp[i-2];
            }
            dp[i]%=mod;
        }
        
        if (n%2==0){
            return (int)dp[n];    
        }else{
            return 0;
        }
        
    }
}