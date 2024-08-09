import java.util.ArrayList;
import java.util.List;

public class ExampleList {
    public void example() {
        List<String> list = new ArrayList<>();
        list.add("Hello");
        list.remove("Hello");
        list.add("Hello");
        list.add("World");
        System.out.println(list.subList(0, 1));
        list.clear();
        list.add("Hello");
        list.add("World");
        System.out.println(list.contains("Hello"));
        System.out.println((list.getFirst()));
        System.out.println((list.getLast()));
        System.out.println(list.reversed());
        System.out.println(list.indexOf("Hello"));
        System.out.println(list.isEmpty());
    }

    public static void main(String[] args) {
        ExampleList example = new ExampleList();
        example.example();
    }
}