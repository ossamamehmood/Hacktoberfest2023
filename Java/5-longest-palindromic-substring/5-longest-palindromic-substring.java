class Solution {
    public String longestPalindrome(String s) {
            
           if (s == null || s.length() <= 1 || s.equals("")) {
                return s;
            }
    
            String longest = s.substring(0, 1);
            for (int i = 0; i < s.length(); i++) {
                String temp = palindromeHelper(s, i, i);  // odd length
                if (temp.length() > longest.length()) {
                    longest = temp;
                }
    
                temp = palindromeHelper(s, i, i + 1);  // even length
                if (temp.length() > longest.length()) {
                    longest = temp;
                }
            }
            return longest;  
        
    }
         
    
        // given a string and the CENTER(S) of the palindrome (i and i+1), find the longest possible palindrome
        // from center, go left and right till characters are same and return the longest palindromic substring
        private static String palindromeHelper(String string, int begin, int end) {
            while (begin >= 0 && end < string.length() && string.charAt(begin) == string.charAt(end)) {
                begin--;
                end++;
            }
            return string.substring(begin + 1, end);
        }
}
