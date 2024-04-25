import java.util.*;
class Solution {
    public int solution(int[][] jobs) {
        int tot=0;
        int time=0;
        int idx=0;
        int cnt=0;
        
        Arrays.sort(jobs,(o1,o2)->o1[0]-o2[0]);
        PriorityQueue<int[]> pq=new PriorityQueue<>((o1,o2)->o1[1]-o2[1]);
        
        while (cnt<jobs.length){
            while (idx<jobs.length && jobs[idx][0]<=time){
                pq.add(jobs[idx++]);
            }
            
            
            if (pq.isEmpty()){
                time=jobs[idx][0];
            }else{
                int[] tmp=pq.poll();
                tot+=tmp[1]+time-tmp[0];
                time+=tmp[1];
                cnt++;
            }
        }
        return tot/jobs.length;
    }
}