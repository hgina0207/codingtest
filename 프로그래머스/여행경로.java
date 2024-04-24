import java.util.*;
class Solution {
    public String[] solution(String[][] tickets) {
        List<String> list=new ArrayList<>();
        boolean[] visited=new boolean[tickets.length];
        Comparator<String[]> comparator=Comparator.comparing((String[] row)->row[0]).thenComparing(row->row[1]);
        Arrays.sort(tickets,comparator);
        dfs("ICN",visited,tickets,list);
        String[] answer = list.toArray(new String[list.size()]);
        return answer;
    }
    
    boolean check_all_visited(boolean[] visited){
        for (boolean v:visited){
            if (!v){
                return false;
            }
        }
        return true;
    }
    boolean dfs(String s, boolean[] visited, String[][] tickets, List<String> list){
        list.add(s);
        if (check_all_visited(visited)){
            return true;
        }else{
            for(int i=0;i<tickets.length;i++){
                if (!visited[i] && s.equals(tickets[i][0])){
                    visited[i]=true;
                    boolean flag=dfs(tickets[i][1],visited,tickets,list);
                    if (flag){
                        return true;
                    }else{
                        visited[i]=false;
                        list.remove(list.size()-1);
                    }
                }
            }
            return false;
        }
    }
}