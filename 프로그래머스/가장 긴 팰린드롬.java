import java.util.*;
class Solution
{
    public int solution(String s)
    {
        int n=s.length();
        for (int len=n;len>1;len--){
            for (int idx=0;idx+len<=n;idx++){
                int start=idx;
                int end=start+len-1;
                boolean flag=true;
                while (start<end){
                    if (s.charAt(start++)!=s.charAt(end--)){
                        flag=false;
                        break;
                    }
                }
                if (flag){
                    return len;
                }
            }
        }

        return 1;
    }
}