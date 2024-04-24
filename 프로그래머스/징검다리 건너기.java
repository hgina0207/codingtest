import java.util.*;
class Solution {
    public int solution(int[] stones, int k) {
        int answer = 0;
        int left=0;
        int right=Integer.MAX_VALUE;
        while (left<=right){     
            int mid=(left+right)/2;
            int cnt=0;
            boolean flag=true;
            for (int i=0;i<stones.length;i++){
                if (stones[i]<mid){
                    cnt++;
                    if (cnt>=k){
                        flag=false;
                        break;
                    }
                }else{
                    cnt=0;
                }
            }
            if (flag){
                answer=mid;
                left=mid+1;
            }else{
                right=mid-1;
            }
        }
        return answer;
    }
}