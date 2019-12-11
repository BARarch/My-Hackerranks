import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] a = new int[n];

        for (int i = 0; i < n; i++) {
            a[i] = scan.nextInt();
        }

        scan.close();

        int nNegSum = 0;
        int sum = 0;

        // Itterate over each sub array of a
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                // Even Case Count Up
                for (int j = i; j < n; j++) {
                    sum += a[j];
                    if (sum < 0) {
                        nNegSum++;
                    }
                }
            } else {
                // Odd Case Count Down
                sum -= a[i - 1];
                for (int j = n - 1; j >= i; j--) {
                    if (sum < 0) {
                        nNegSum++;
                    }
                    sum -= a[j];
                }
            }
        }
        System.out.println(nNegSum);
    }
}

