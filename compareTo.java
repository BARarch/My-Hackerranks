import java.util.Scanner;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "z";
        String largest = "";

        for (int j = k; j <= s.length(); j++) {
            int i = j - k;
            if (smallest.compareTo(s.substring(i, j)) > 0) {
                smallest = s.substring(i, j);
            }
            if (largest.compareTo(s.substring(i, j)) < 0) {
                largest = s.substring(i, j);
            }
        }
        
        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        
        return smallest + "\n" + largest;
    }

