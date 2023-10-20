import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class DuplicateWordCount {

    public static void main(String[] args) {
        String str = "hello there hello hi there hello";
        String[] strArr = str.split(" ");

        HashMap<String, Integer> hashMap = new HashMap<>();
        for (String s : strArr) {
            Integer count = hashMap.get(s);
            hashMap.put(s, count == null ? 1 : count + 1);
        }

        Map<String, Integer> hashMapCountGreaterThanTwo = hashMap.entrySet().stream()
                .filter(entry -> entry.getValue() > 1)
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));

        System.out.println(hashMapCountGreaterThanTwo);
    }
}
