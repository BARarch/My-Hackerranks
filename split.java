import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        if(!scan.hasNext()) { 
            System.out.print("0"); 
            return; 
        }
        String s = scan.nextLine();
        // Write your code here.
        String[] tokens = s.trim().split("[ !,?._'@]+");
        System.out.println(tokens.length);
        for (String token: tokens) {
            System.out.println(token);
        }
        scan.close();
    }
}

