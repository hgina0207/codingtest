import java.util.*;
class test{
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("apple");
        list.add("banana");
        list.add("orange");

        // List를 배열로 변환
        String[] array = list.toArray(new String[list.size()]);

        // 배열 출력
        for (String element : array) {
            System.out.println(element);
        }
    }
}

