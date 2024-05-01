import java.util.*;
public class 더맵게 {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq=new PriorityQueue<>();
        for (int s:scoville){
            pq.add(s);
        }
        if (pq.peek()>=K){
            return 0;
        }
        while (pq.size()>=2 && !check(pq,K)){
            int a=pq.poll();
            int b=pq.poll();
            int newScoville=a+2*b;
            pq.add(newScoville);
            answer++;
        }
        
        if(check(pq,K)){
            return answer;
        }
        else{
            return -1;    
        }
        
    }
    boolean check(PriorityQueue<Integer> pq,int K){
        for (int n:pq){
            if (n<K){
                return false;
            }
        }
        return true;
    }
}
