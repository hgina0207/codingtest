import java.util.*;
class Solution {
    public int solution(int[][] board) {
        int answer = Integer.MAX_VALUE;
        int n=board.length;
        
        int[] dx={1,-1,0,0};
        int[] dy={0,0,1,-1};
        
        for(int i=0;i<board.length;i++){
            for (int j=0;j<board.length;j++){
                if(board[i][j]==0) board[i][j]=Integer.MAX_VALUE;
            }
        }
        
        PriorityQueue<int[]> pq=new PriorityQueue<>((o1,o2)->o1[0]-o2[0]);
        int[][][] visited=new int[n][n][4];
        
        pq.add(new int[]{0,0,0,-1});
        
        while (!pq.isEmpty()){
            int[] info=pq.poll();
            int cost=info[0];
            int y=info[1];
            int x=info[2];
            int direc=info[3];
            
            
            if (x==n-1 && y==n-1){
                if (answer>cost){
                    answer=cost;
                }
                continue;
            }
            
            for (int i=0;i<4;i++){
                int ny=y+dy[i];
                int nx=x+dx[i];
                if ((nx>=0 && nx<n) && (ny>=0 && ny<n) && board[ny][nx]!=1){
                    int next_cost=cal_cost(cost,direc,i);
                    if (visited[ny][nx][i]==0 || next_cost<=board[ny][nx]){
                        board[ny][nx]=next_cost;
                        visited[ny][nx][i]=1;
                        pq.add(new int[]{next_cost,ny,nx,i});
                    }
                }
            }
        }
        return answer;
    }
    int cal_cost(int cost,int direc,int next_direc){
        if (next_direc==direc || direc==-1){
            return cost+100;
        }else{
            return cost+600;
        }
    }
}