

import java.util.*;

public class Permutation {
    public static void main(String[] args) {
        String s = "abc";
        String empty = "";
        perm(s, empty);
    }

    static void perm(String s, String empty) {
        if (s.isEmpty()) {
            System.out.println(empty);
            return;
        }
        char ch = s.charAt(0);
        for (int i = 0; i <= empty.length(); i++) {
            perm(s.substring(1), empty.substring(0, i) + ch + empty.substring(i, empty.length()));
        }
    }
}
