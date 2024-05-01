import java.util.*;
class Solution {
    public int[] solution(int[][] edges) {
        int[] answer = {0,0,0,0};
        Map<Integer,int[]> map=new HashMap<>();
        
        for(int[] e:edges){
            int a=e[0];
            int b=e[1];
            
            if (!map.containsKey(a)){
                map.put(a,new int[]{0,0});
            }
            if (!map.containsKey(b)){
                map.put(b,new int[]{0,0});
            }
            map.get(a)[0]++;
            map.get(b)[1]++;
        }
        
        map.forEach((k,v)->{
            if (v[0]>=2 && v[1]==0){
                answer[0]=k;
            }else if(v[0]==0 && v[1]>=1){
                answer[2]++;
            }else if(v[0]>=2 && v[1]>=2){
                answer[3]++;
            }
        });
        answer[1]=map.get(answer[0])[0]-answer[2]-answer[3];
        return answer;
    }
}