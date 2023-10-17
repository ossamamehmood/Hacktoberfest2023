// https://leetcode.com/problems/valid-anagram/
/* Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters. */

class valid_anagram {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int characters[] = new int[26];
        for (int i = 0; i < s.length(); i++) {
            characters[s.charAt(i) - 'a']++;
            characters[t.charAt(i) - 'a']--;
        }
        for (int alphabet : characters) {
            if (alphabet != 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String args[]) {
        String s = "anagram";
        String t = "nagaram";
        valid_anagram va = new valid_anagram();
        System.out.println(va.isAnagram(s, t));
    }
}