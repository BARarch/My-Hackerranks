import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int[][] arr = new int[6][6];

        for (int i = 0; i < 6; i++) {
            String[] arrRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 6; j++) {
                int arrItem = Integer.parseInt(arrRowItems[j]);
                arr[i][j] = arrItem;
            }
        }

        int maxSum = -63;
        for (int i = 1; i < 5; i++){
            for (int j = 1; j < 5; j++) {
                int s = arr[i][j];
                s += arr[i - 1][j - 1];
                s += arr[i - 1][j];
                s += arr[i - 1][j + 1];
                s += arr[i + 1][j - 1];
                s += arr[i + 1][j];
                s += arr[i + 1][j + 1];
                //System.out.println(s);
                if (s > maxSum) {
                    maxSum = s;
                }
            }
        }
        System.out.println(maxSum);
        scanner.close();
    }
}
