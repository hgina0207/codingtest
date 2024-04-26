import java.util.*;
class Solution {
    public long solution(int[] sequence) {
        long answer = 0;
        boolean isPlus=true;
        
        long p1=0;
        long p2=0;
        
        for (int num : sequence){
            p1+=isPlus? num : -num;
            p2+=isPlus? -num : num;
            
            p1=Math.max(0,p1);
            p2=Math.max(0,p2);
            
            answer=Math.max(answer,Math.max(p1,p2));
            
            isPlus=!isPlus;
        }
        return answer;
    }
}