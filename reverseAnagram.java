import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        
        int j = A.length();
        for (int i = 0; i < A.length(); i++) {
            if (A.charAt(i) != A.charAt(--j)) {
                System.out.println("No");
                return;
            }
        }
        System.out.println("Yes");
    }
}



