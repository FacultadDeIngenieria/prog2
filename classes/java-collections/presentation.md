class: center, middle, inverse

# Java collections
Examples of Java collections

---

# Java Collections

## List

```java
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
        ...
        
```

---

# Java Collections

## List

```java
   {
    ...
        for (String element : list) {
            System.out.println(element);
        }
        
        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i));
        }
        
        int i = 0;
        while (i < list.size()) {
            System.out.println(list.get(i));
            i++;
        }
    }
```

---

# Java Collections

## Set

```java
 public void example() {
        Set<String> set = new HashSet<>();
        set.add("Hello");
        set.remove("Hello");
        set.add("Hello");
        set.add("World");
        System.out.println(set.contains("Hello"));
        System.out.println(set.isEmpty());
        
        for (String element : set) {
            System.out.println(element);
        }
        
        for (int i = 0; i < set.size(); i++) {
            System.out.println(set.get(i));
        }
        
        int i = 0;
        while (i < set.size()) {
            System.out.println(set.get(i));
            i++;
        }
    }
```

---

# Java Collections

## Map

```java
 public void example() {
        Map<String, String> map = new HashMap<>();
        map.put("Hello", "World");
        map.remove("Hello");
        map.put("Hello", "World");
        System.out.println(map.get("Hello"));
        System.out.println(map.containsKey("Hello"));
        System.out.println(map.containsValue("World"));
        System.out.println(map.isEmpty());
        
        for (String key : map.keySet()) {
            System.out.println(key + " -> " + map.get(key));
        }
        
        for (String value : map.values()) {
            System.out.println(value);
        }
        
        for (Map.Entry<String, String> entry : map.entrySet()) {
            System.out.println(entry.getKey() + " -> " + entry.getValue());
        }
    }
```