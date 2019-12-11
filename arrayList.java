import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        
        ArrayList<Integer>[] a = new ArrayList[n + 1];
        // Set List
        for (int i = 0; i < n + 1; i++) {
            String line = scan.nextLine();
            Scanner lineScanner = new Scanner(line);
            a[i] = new ArrayList<Integer>();
            while (lineScanner.hasNext()) {
                a[i].add(lineScanner.nextInt());
            }
        }
        int m = scan.nextInt();
        //System.out.println(m);
        for (int j = 0; j < m; j++) {
            //System.out.println(a[5].size());
            int k = scan.nextInt();
            int l = scan.nextInt();
            if (k <= a.length) {
                if (l < a[k].size()) {
                    System.out.println(a[k].get(l));
                } else {
                    System.out.println("ERROR!");
                }
            } else {
                System.out.println("ERROR!");
            }
        }
    }
}

