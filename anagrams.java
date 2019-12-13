import java.util.Scanner;

public class Solution {
    static boolean isAnagram(String a, String b) {
        java.util.List<Character> A = new java.util.ArrayList<Character>();
        char[] charsA = a.toLowerCase().toCharArray();
        char[] charsB = b.toLowerCase().toCharArray();

        for (char ch : charsA) {
            A.add(ch);
        }

        for (char ch : charsB) {
            if (A.indexOf(ch) >= 0) {
                A.remove(A.indexOf(ch));
            } else {
                return false;
            }
        }

        if (A.size() > 0) {
            return false;
        } else {
            return true;
        }

    }

  public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
